from sgae_app.domain.exceptions.exceptions import ResourceNotFoundException
from sgae_app.domain.repositories.secretary_repository import SecretaryRepository
from sgae_app.domain.entities.secretary import Secretary
from auth_app.models import User

class CreateSecretary:
    def __init__(self, repository: SecretaryRepository):
        self.repository = repository

    def execute(self, secretary: Secretary) -> Secretary:
        if self.repository.exists(secretary.email):
            raise ResourceNotFoundException(f"Secretary with email {secretary.email} already exists.")

        user = User.objects.create(
            username=secretary.email,
            password=secretary.id_card,
            user_type='secretary'
        )

        secretary.user = user
        self.repository.save(secretary)
        return secretary


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

    def execute(self, secretary_id: int, first_name: str, last_name: str, email: str) -> Secretary:
        secretary = self.repository.get_by_id(secretary_id)
        if not secretary:
            raise ResourceNotFoundException(f"Secretary with id {secretary_id} not found.")

        secretary.first_name = first_name
        secretary.first_lastname = last_name
        secretary.email = email
        self.repository.save(secretary)
        return secretary


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