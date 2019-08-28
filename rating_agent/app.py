from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .routers import agent
from .routers import graphql
from .routers import status
from .services import bus as bus_service


def get_app(config: dict):
    app = FastAPI(
        title="rating-agent",
        description="Rating Engine: Agent API",
        version="1.0.0",
        openapi_url="/v1/openapi.json",
    )
    setattr(app, 'config', config)

    app.include_router(
        agent.router, prefix='/v1', tags=['agent'],
    )
    app.include_router(graphql.router)
    app.include_router(status.router, tags=['status'])

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app = bus_service.setup(app, config)

    return app
