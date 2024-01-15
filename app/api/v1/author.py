from fastapi import APIRouter, Depends
from fastapi_pagination import Page
from sqlmodel import Session
from app.models import engine
from app.models.author import Author, CreateAuthor, AuthorSchema, FindAuthor
from app.services.author_service import AuthorService
import typing

router = APIRouter(prefix="/author")


@router.get("/", response_model=Page[AuthorSchema])
def get_authors(service: typing.Annotated[AuthorService, Depends(AuthorService)], find: FindAuthor = Depends()):
    return service.get_by_options(find)


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
