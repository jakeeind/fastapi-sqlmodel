from .base import BaseService
from api.repositories.author import AuthorRepository
from fastapi import Depends
from api.models import get_session


class AuthorService(BaseService):
    def __init__(self, author_repository: AuthorRepository = AuthorRepository(session=Depends(get_session))):
        self.author_repository = author_repository
        super().__init__(self.author_repository)
