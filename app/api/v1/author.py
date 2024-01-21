from fastapi import APIRouter, Depends
from fastapi_pagination import Page
from app.models.author import CreateAuthor, AuthorSchema, FindAuthor
from app.services.author_service import AuthorService
# from fastapi_pagination.ext.sqlmodel import paginate
# from sqlmodel import Session
# from app.models import get_session
import typing

router = APIRouter(prefix="/author", tags=["Author"])


@router.get("/", response_model=Page[AuthorSchema])
def get_authors(
    service: typing.Annotated[AuthorService, Depends(AuthorService)],
    # session: Depends(get_session),
    find: FindAuthor = Depends(),
):
    return service.get_by_options(find)


@router.post("/", response_model=AuthorSchema)
def create_author(author_info: CreateAuthor, service: typing.Annotated[AuthorService, Depends(AuthorService)]):
    return service.create(author_info)


@router.get("/{author_id}", response_model=AuthorSchema)
def get_author(author_id: int, service: typing.Annotated[AuthorService, Depends(AuthorService)]):
    return service.get_by_id(author_id)


@router.patch("/{author_id}", response_model=AuthorSchema)
def update_author(
    author_id: int, author_info: CreateAuthor, service: typing.Annotated[AuthorService, Depends(AuthorService)]
):
    return service.update(author_id, author_info)


@router.delete("/{author_id}", response_model=AuthorSchema)
def delete_author(author_id: int, service: typing.Annotated[AuthorService, Depends(AuthorService)]):
    return service.delete(author_id)
