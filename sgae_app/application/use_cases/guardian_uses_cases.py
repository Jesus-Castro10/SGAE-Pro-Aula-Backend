from sgae_app.domain.entities.guardian import Guardian
from sgae_app.domain.repositories.guardian_repository import GuardianRepository
from auth_app.models import User

from sgae_app.domain.exceptions.exceptions import (DuplicateKeyException,
    ResourceNotFoundException, UserAlreadyExistsException)
from sgae_app.domain.utils.mapping import person_mapper

class CreateGuardian:
    def __init__(self, repository: GuardianRepository):
        self.repository = repository

    def _exists(self, guardian: Guardian) -> None:
        if self.repository.get_by_id_card(guardian.id_card):
            guardian.user.delete()
            raise UserAlreadyExistsException(
                f"Guardian with id card {guardian.id_card} already exists."
            )
        
    def execute(self, guardian: Guardian) -> Guardian:
        self._exists(guardian)
        return self.repository.save(guardian)

class GetGuardian:
    def __init__(self, repository: GuardianRepository):
        self.repository = repository

    def execute(self, guardian_id: int):
        guardian = self.repository.get_by_id(guardian_id)
        if not guardian:
            raise ResourceNotFoundException(f"Guardian with id {guardian_id} not found.")
        return guardian


class UpdateGuardian:
    def __init__(self, repository: GuardianRepository):
        self.repository = repository

    def execute(self, guardian_id: int, update_data: Guardian):
        guardian_db = self.repository.get_by_id(guardian_id)
        if not guardian_db:
            raise ResourceNotFoundException(f"Guardian with id {guardian_id} not found.")
        
        person_mapper(guardian_db,update_data)
        
        return self.repository.save(guardian_db)


class DeleteGuardian:
    def __init__(self, repository: GuardianRepository):
        self.repository = repository

    def execute(self, guardian_id: int):
        guardian = self.repository.get_by_id(guardian_id)
        if not guardian:
            raise ResourceNotFoundException(f"Guardian with id {guardian_id} not found.")

        self.repository.delete(guardian_id)
        return guardian
    
class GetAllGuardians:
    def __init__(self, repository: GuardianRepository):
        self.repository = repository

    def execute(self):
        guardians = self.repository.get_all()
        if not guardians:
            raise ResourceNotFoundException("No guardians found.")
        return guardians