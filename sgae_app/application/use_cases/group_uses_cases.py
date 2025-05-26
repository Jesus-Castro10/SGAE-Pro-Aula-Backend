from sgae_app.domain.exceptions.exceptions import DuplicateKeyException, ResourceNotFoundException
from sgae_app.domain.utils.mapping import mapper as group_mapper

class CreateGroup:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, group):
        if self.repository.exists(group):
            raise DuplicateKeyException("Group already exists.")
        return self.repository.save(group)

class GetGroup:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, group_id: int):
        group = self.repository.get_by_id(group_id)
        if not group:
            raise ResourceNotFoundException("Group not found.")
        return group

class GetAllGroups:
    def __init__(self, repository):
        self.repository = repository

    def execute(self):
        groups = self.repository.get_all()
        if not groups:
            raise ResourceNotFoundException("No groups found.")
        return groups

class UpdateGroup:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, group_id: int, update_data):
        group_db = self.repository.get_by_id(group_id)
        if not group_db:
            raise ResourceNotFoundException("Group not found.")
        group_mapper(group_db, update_data, fields=["name", "year","section","turn","registered_at"])
        return self.repository.save(group_db)

class DeleteGroup:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, group_id: int):
        if not self.repository.get_by_id(group_id):
            raise ResourceNotFoundException("Group not found.")
        self.repository.delete(group_id)
