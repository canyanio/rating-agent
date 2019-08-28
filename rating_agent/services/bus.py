import json

from typing import Any, Callable, Optional

from aio_pika import connect_robust, Channel, Connection
from aio_pika.patterns import RPC
from fastapi import FastAPI
from starlette.requests import Request


class JsonRPC(RPC):
    SERIALIZER = json
    CONTENT_TYPE = 'application/json'

    def deserialize(self, data: bytes) -> Any:
        return self.SERIALIZER.loads(data.decode('utf-8'))

    def serialize(self, data: Any) -> bytes:
        return self.SERIALIZER.dumps(data, ensure_ascii=False, default=repr).encode(
            'utf-8'
        )


class BusService(object):
    connection: Connection
    channel: Channel
    rpc: JsonRPC

    def __init__(self, messagebus_uri: str):
        self._messagebus_uri = messagebus_uri

    async def connect(self):
        self.connection = await connect_robust(self._messagebus_uri)
        self.channel = await self.connection.channel()
        self.rpc = await JsonRPC.create(self.channel)

    async def close(self):
        await self.connection.close()

    async def rpc_call(
        self, method: str, kwargs: dict, expiration: int = 10
    ) -> Optional[dict]:
        return await self.rpc.call(method, kwargs=kwargs, expiration=expiration)

    async def rpc_register(self, method: str, func: Callable, auto_delete: bool = True):
        await self.rpc.register(method, func, auto_delete=auto_delete)


def get(request: Request) -> BusService:
    return request.state.bus


def setup(app: FastAPI, config: dict) -> FastAPI:
    bus_service = BusService(messagebus_uri=config["messagebus_uri"])
    setattr(app, "bus_service", bus_service)

    app.add_event_handler("startup", bus_service.connect)
    app.add_event_handler("shutdown", bus_service.close)

    @app.middleware("http")
    async def storage_middleware(request: Request, call_next):
        request.state.bus = bus_service
        response = await call_next(request)
        return response

    _ = storage_middleware

    return app
