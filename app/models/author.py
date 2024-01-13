import typing
from datetime import datetime
from sqlmodel import Field, SQLModel
from sqlalchemy import Column, TIMESTAMP


class BaseAuthor(SQLModel):
    full_name: str = Field(index=True, max_length=128)
    pseudonym: str = Field(index=True, max_length=128)


class Author(BaseAuthor, table=True):
    __tablename__ = "authors"
    id: typing.Optional[int] = Field(default=None, primary_key=True)
    created_date: datetime = Field(sa_column=Column(TIMESTAMP, default=datetime.utcnow))
    updated_date: datetime = Field(sa_column=Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow))

    class Config:
        orm_mode = True


class AuthorSchema(BaseAuthor):
    id: int
    created_date: datetime
    updated_date: datetime


class FindAuthor(BaseAuthor):
    pass


class CreateAuthor(BaseAuthor):
    pass
