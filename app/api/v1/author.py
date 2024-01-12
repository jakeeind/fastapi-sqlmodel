from fastapi import APIRouter
from sqlmodel import Session, select
from app.models import engine
from app.models.author import Author, CreateAuthor, AuthorSchema

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
