import asyncio
import os
import pytest

from queue import Empty

MESSAGEBUS_URI = os.getenv("MESSAGEBUS_URI", "pyamqp://user:password@localhost:5672//")

API_URL = os.getenv("API_URL", "http://localhost:8000/graphql")
API_USERNAME = os.getenv("API_USERNAME", "username")
API_PASSWORD = os.getenv("API_PASSWORD", "password")


def run_synchronously(coroutine):
    event_loop = None
    try:
        event_loop = asyncio.get_event_loop()
    except RuntimeError:
        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)
    return event_loop.run_until_complete(coroutine)


@pytest.fixture(scope="function")
def app():
    from rating_agent.app import get_app

    config = dict(
        messagebus_uri=MESSAGEBUS_URI,
        api_url=API_URL,
        api_username=API_USERNAME,
        api_password=API_PASSWORD,
        debug=True,
    )
    return get_app(config)


@pytest.fixture(scope="function")
def client(app):
    from starlette.testclient import TestClient

    cli = TestClient(app)
    with cli:
        yield cli


def engine_fake_method():
    def _method(*, request: dict) -> dict:
        from rating_agent.tests.common import EngineTestingQueue

        try:
            item = EngineTestingQueue.get_nowait()
        except Empty:
            return {}
        return item

    return _method


@pytest.fixture(scope="function")
def engine():
    from rating_agent.enums import MethodName
    from rating_agent.services import bus as bus_service

    bus = bus_service.BusService(MESSAGEBUS_URI)
    run_synchronously(bus.connect())
    run_synchronously(
        bus.rpc_register(MethodName.AUTHORIZATION.value, engine_fake_method())
    )
    run_synchronously(
        bus.rpc_register(MethodName.BEGIN_TRANSACTION.value, engine_fake_method())
    )
    run_synchronously(
        bus.rpc_register(MethodName.END_TRANSACTION.value, engine_fake_method())
    )
    run_synchronously(
        bus.rpc_register(MethodName.ROLLBACK_TRANSACTION.value, engine_fake_method())
    )
    run_synchronously(
        bus.rpc_register(MethodName.RECORD_TRANSACTION.value, engine_fake_method())
    )
    try:
        yield
    finally:
        run_synchronously(bus.close())
