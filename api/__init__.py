from contextlib import asynccontextmanager
from fastapi import FastAPI
from api.router import init_router
from api.models import init_db_and_tables, close_db_connection
from api.core.app import get_app_settings, AppSettings
from fastapi_pagination.api import _add_pagination


def create_app():
    app = FastAPI()
    settings: AppSettings = get_app_settings()
    settings.configure_logging()

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        await init_router(app, settings=settings)
        init_db_and_tables()
        _add_pagination(app)
        yield
        close_db_connection()

    app.router.lifespan_context = lifespan

    @app.get("/", tags=["Root"])
    async def healthy():
        return {"status": "healthy"}

    return app
