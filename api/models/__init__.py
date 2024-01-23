from sqlmodel import create_engine, SQLModel, Session
from api.core.app import get_app_settings
from .author import Author

__all__ = [
    "Author",
]

settings = get_app_settings()

engine = create_engine(settings.DB_URI, echo=settings.DEBUG, future=True)

def get_session():
    with Session(engine) as session:
        try:
            yield session
        except:
            session.rollback()
            raise
        finally:
            session.close()


def init_db_and_tables():
    SQLModel.metadata.create_all(engine)


def close_db_connection():
    engine.dispose()
