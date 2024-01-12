from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api import init_router
from app.models import init_db_and_tables, close_db_connection
from app.core.app import get_app_settings, AppSettings


def create_app():
    app = FastAPI()
    settings: AppSettings = get_app_settings()
    settings.configure_logging()

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        await init_router(app, settings=settings)
        init_db_and_tables()
        yield
        close_db_connection()

    app.router.lifespan_context = lifespan

    @app.get("/", tags=["Root"])
    async def healthy():
        return {"status": "healthy"}

    return app


app = create_app()
