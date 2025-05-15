from sgae_app.domain.entities.guardian import Guardian
from sgae_app.domain.repositories.guardian_repository import GuardianRepository
from auth_app.models import User

from sgae_app.domain.exceptions.exceptions import (DuplicateKeyException,
    ResourceNotFoundException, UserAlreadyExistsException)

class CreateGuardian:
    def __init__(self, repository: GuardianRepository):
        self.repository = repository

    def execute(
        self,
        guardian: Guardian
    ) -> Guardian:
        if self.repository.exists(guardian):
            raise UserAlreadyExistsException(f"Guardian already exists check the id card or email.")
        
        try:
            user = User.objects.create(
                username=guardian.email,
                user_type='guardian'
            ) #Create service to create user
            user.set_password(guardian.id_card)
            user.save()
            guardian.user = user
            self.repository.save(guardian)
        except Exception as e:
            user.delete()
            raise DuplicateKeyException(errors={str(e)})
        return guardian

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

    def execute(self, guardian_id: int, guardian: Guardian):
        guardian_db = self.repository.get_by_id(guardian_id)
        if not guardian_db:
            raise ResourceNotFoundException(f"Guardian with id {guardian_id} not found.")
        
        self.repository.save(guardian)
        return guardian


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