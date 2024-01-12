from sqlmodel import create_engine, SQLModel

engine = create_engine("postgresql://admin:!q2w3e4r5t@localhost:5432/fastapi_sqlmodel")


def init_db_and_tables():
    SQLModel.metadata.create_all(engine)


def close_db_connection():
    engine.dispose()
