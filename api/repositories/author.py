from api.models.author import Author
from .base import BaseRepository
from sqlmodel import Session


class AuthorRepository(BaseRepository):
    def __init__(self, session: Session) -> None:
        super().__init__(Author, session)
