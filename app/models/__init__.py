from sqlmodel import create_engine, SQLModel
from app.core.app import get_app_settings

settings = get_app_settings()
engine = create_engine(
    "{db_engine}://{user}:{password}@{host}:{port}/{database}".format(
        db_engine=settings.DB_ENGINE_MAPPER[settings.DB],
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
        host=settings.DB_HOST,
        port=settings.DB_PORT,
        database=settings.DB_NAME,
    ),
    echo=settings.DEBUG,
)


def init_db_and_tables():
    SQLModel.metadata.create_all(engine)


def close_db_connection():
    engine.dispose()
