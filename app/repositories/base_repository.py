from sqlmodel import Session, select
from app.core.exceptions import DuplicatedError, NotFoundError
from sqlmodel import SQLModel
from sqlalchemy.exc import IntegrityError
from fastapi_pagination.ext.sqlmodel import paginate
from app.utils.query_builder import dict_to_sqlalchemy_filter_options
from app.models import get_session

session = get_session()


class BaseRepository:
    def __init__(self, model, session: Session = get_session().__next__()) -> None:
        self.model = model
        self.session = session

    def read_by_id(self, id: int):
        query = self.session.get(self.model, id)
        if not query:
            raise NotFoundError(detail=f"{self.model.__name__} with id {id} not found")
        return query

    def read_by_options(self, schema: SQLModel):
        schema_dict = schema.model_dump(exclude_none=True)
        filter_options = dict_to_sqlalchemy_filter_options(self.model, schema_dict)
        return paginate(self.session, select(self.model).where(filter_options))

    def create(self, schema: SQLModel):
        model = self.model(**schema.model_dump())
        try:
            self.session.add(model)
            self.session.commit()
            self.session.refresh(model)
        except IntegrityError as e:
            self.session.rollback()
            raise DuplicatedError(detail=str(e.orig))
        return model

    def update(self, id: int, schema: SQLModel):
        query = self.session.get(self.model, id)
        if not query:
            raise NotFoundError(detail=f"{self.model.__name__} with id {id} not found")
        schema_dict = schema.model_dump(exclude_none=True)
        for key, value in schema_dict.items():
            setattr(query, key, value)
        self.session.add(query)
        self.session.commit()
        self.session.refresh(query)
        return query

    def delete(self, id: int):
        query = self.session.get(self.model, id)
        if not query:
            raise NotFoundError(detail=f"{self.model.__name__} with id {id} not found")
        self.session.delete(query)
        self.session.commit()
        return query
