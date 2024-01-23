from api.models.author import Author
from .base import BaseRepository
from fastapi import Depends
from sqlmodel import Session
from api.models import get_session


class AuthorRepository(BaseRepository):
    def __init__(self, session: Session = Depends(get_session)) -> None:
        super().__init__(Author, session)
