from app.repositories.base import BaseRepository


class BaseService:
    def __init__(self, repository: BaseRepository):
        self.repository = repository

    def get_by_id(self, id: int):
        return self.repository.read_by_id(id)

    def get_by_options(self, schema):
        return self.repository.read_by_options(schema)

    def create(self, schema):
        return self.repository.create(schema)

    def update(self, id: int, schema):
        return self.repository.update(id, schema)

    def delete(self, id: int):
        return self.repository.delete(id)
