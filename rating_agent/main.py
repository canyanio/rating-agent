import click
import uvicorn  # type: ignore

from typing import Optional

from .app import get_app


@click.command()
@click.option("-h", "--host", type=click.STRING, default="0.0.0.0", show_default=True)
@click.option("-p", "--port", type=click.INT, default=8000, show_default=True)
@click.option(
    "--messagebus-uri",
    type=click.STRING,
    default="pyamqp://user:password@localhost:5672//",
    show_default=True,
)
@click.option(
    "--api-url", type=click.STRING, default="http://localhost:8000", show_default=True,
)
@click.option(
    "--api-username", type=click.STRING, default=None,
)
@click.option(
    "--api-password", type=click.STRING, default=None,
)
@click.option(
    "--jwt/--no-jwt",
    default=False,
    help='enable JWT-based authentication and authorization',
)
@click.option(
    "--jwt-issuer", type=click.STRING, default="rating.canyan.io", show_default=True
)
@click.option(
    "--jwt-secret-key",
    type=click.STRING,
    default=None,
    show_default=False,
    help='set the JWT secret key, defaults to a randomly generated string',
)
@click.option("-d", "--debug/--no-debug", default=False)
def main(
    host: str = "0.0.0.0",
    port: int = 8000,
    messagebus_uri: str = "pyamqp://user:password@localhost:5672//",
    api_url: str = None,
    api_username: Optional[str] = None,
    api_password: Optional[str] = None,
    jwt: bool = False,
    jwt_issuer: str = "rating.canyan.io",
    jwt_secret_key: Optional[str] = None,
    debug: bool = False,
    **kw,
):
    config = dict(
        host=host,
        port=port,
        messagebus_uri=messagebus_uri,
        api_url=api_url,
        api_username=api_username,
        api_password=api_password,
        jwt=jwt,
        jwt_issuer=jwt_issuer,
        jwt_secret_key=jwt_secret_key,
        debug=debug,
    )
    app = get_app(config)
    log_level = "info" if not config["debug"] else "debug"
    uvicorn.run(
        app,
        host=config["host"],
        port=config["port"],
        log_level=log_level,
        reload=config["debug"],
    )


def main_with_env():  # pragma: no cover
    main(auto_envvar_prefix="RATING_AGENT")
