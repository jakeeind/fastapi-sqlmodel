from sqlmodel import Session, select
from app.models import engine
from app.core.exceptions import NotFoundError
from sqlmodel import SQLModel
from fastapi_pagination.ext.sqlmodel import paginate
from typing import TypeVar

T = TypeVar("T")


class BaseRepository:
    def __init__(self, model) -> None:
        # self.session_factory = session_factory
        self.model = model

    def read_by_id(self, id: int):
        with Session(engine) as session:
            query = session.get(self.model, id)
            if not query:
                return NotFoundError(detail=f"{self.model.__name__} with id {id} not found")
            return query

    def read_by_options(self, schema: SQLModel):
        with Session(engine) as session:
            return paginate(session, select(self.model))
