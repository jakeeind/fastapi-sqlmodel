from .base_service import BaseService
from app.repositories.author_repository import AuthorRepository


class AuthorService(BaseService):
    def __init__(self):
        self.author_repository = AuthorRepository()
        super().__init__(self.author_repository)
