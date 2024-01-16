from app.repositories.base_repository import BaseRepository


class BaseService:
    def __init__(self, repository: BaseRepository):
        self._repository = repository

    def get_by_id(self, id: int):
        return self._repository.read_by_id(id)

    def get_by_options(self, schema):
        return self._repository.read_by_options(schema)

    def create(self, schema):
        return self._repository.create(schema)

    def update(self, id: int, schema):
        return self._repository.update(id, schema)

    def delete(self, id: int):
        return self._repository.delete(id)
