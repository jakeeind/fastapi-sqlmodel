from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from app.models import engine
from app.models.author import Author, CreateAuthor, AuthorSchema
from app.services.author_service import AuthorService
import typing

router = APIRouter(prefix="/author")


@router.get("/")
def get_authors():
    with Session(engine) as session:
        authors = session.exec(select(Author)).all()
        return authors


@router.post("/", response_model=AuthorSchema)
def create_author(author_info: CreateAuthor):
    with Session(engine) as session:
        author = Author(**author_info.model_dump())
        session.add(author)
        session.commit()
        session.refresh(author)
        return author


@router.get("/{author_id}", response_model=AuthorSchema)
def get_author(author_id: int, service: typing.Annotated[AuthorService, Depends(AuthorService)]):
    return service.get_by_id(author_id)
