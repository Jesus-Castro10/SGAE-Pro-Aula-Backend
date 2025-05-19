from auth_app.models import User
from sgae_app.domain.entities.secretary import Secretary
from sgae_app.domain.exceptions.exceptions import (
    ResourceNotFoundException,
    UserAlreadyExistsException,
)
from sgae_app.domain.repositories.secretary_repository import SecretaryRepository
from sgae_app.domain.utils.mapping import person_mapper


class CreateSecretary:
    def __init__(self, repository: SecretaryRepository):
        self.repository = repository

    def _exists(self, secretary: Secretary) -> None:
        if self.repository.get_by_id_card(secretary.id_card):
            secretary.user.delete()
            raise UserAlreadyExistsException(
                f"Secretary with id card {secretary.id_card} already exists."
            )
        
    def execute(self, secretary: Secretary) -> Secretary:
        self._exists(secretary)
        try:
            return self.repository.save(secretary)
        except Exception as e:
            secretary.user.delete()
            raise ResourceNotFoundException(f"Error saving secretary: {str(e)}")

class GetSecretary:
    def __init__(self, repository: SecretaryRepository):
        self.repository = repository

    def execute(self, secretary_id: int) -> Secretary:
        secretary = self.repository.get_by_id(secretary_id)
        if not secretary:
            raise ResourceNotFoundException(f"Secretary with id {secretary_id} not found.")
        return secretary


class UpdateSecretary:
    def __init__(self, repository: SecretaryRepository):
        self.repository = repository

    def execute(self, secretary_id: int, secretary_upd: Secretary) -> Secretary:
        secretary_db = self.repository.get_by_id(secretary_id)
        if not secretary_db:
            raise ResourceNotFoundException(f"Secretary with id {secretary_id} not found.")

        person_mapper(secretary_db, secretary_upd)
        
        return self.repository.save(secretary_db)


class DeleteSecretary:
    def __init__(self, repository: SecretaryRepository):
        self.repository = repository

    def execute(self, secretary_id: int) -> Secretary:
        secretary = self.repository.get_by_id(secretary_id)
        if not secretary:
            raise ResourceNotFoundException(f"Secretary with id {secretary_id} not found.")

        self.repository.delete(secretary_id)
        return secretary


class GetAllSecretaries:
    def __init__(self, repository: SecretaryRepository):
        self.repository = repository

    def execute(self) -> list[Secretary]:
        secretaries = self.repository.get_all()
        if not secretaries:
            raise ResourceNotFoundException("No secretaries found.")
        return secretaries