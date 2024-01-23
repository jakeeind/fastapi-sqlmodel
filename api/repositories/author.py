from api.models.author import Author
from .base import BaseRepository


class AuthorRepository(BaseRepository):
    def __init__(self) -> None:
        super().__init__(Author)
