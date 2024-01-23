from .base import BaseService
from api.repositories.author import AuthorRepository
from fastapi import Depends


class AuthorService(BaseService):
    def __init__(self, author_repository: AuthorRepository = Depends(AuthorRepository)):
        self.author_repository = author_repository
        super().__init__(self.author_repository)
