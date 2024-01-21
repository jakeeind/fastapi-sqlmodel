from app.models.author import Author
from .base_repository import BaseRepository


class AuthorRepository(BaseRepository):
    def __init__(self) -> None:
        super().__init__(Author)
