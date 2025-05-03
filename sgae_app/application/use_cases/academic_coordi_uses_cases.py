from sgae_app.domain.exceptions.exceptions import ResourceNotFoundException, UserWithEmailAlreadyExistsException
from sgae_app.domain.repositories.academic_coordinator_repo import AcademicCoordinatorRepository
from sgae_app.domain.entities.academic_coordinator import AcademicCoordinator
from auth_app.models import User

class CreateAcademicCoordinator:
    def __init__(self, repository: AcademicCoordinatorRepository):
        self.repository = repository

    def execute(self, academic_coordinator: AcademicCoordinator) -> AcademicCoordinator:
        if self.repository.exists(academic_coordinator.email):
            raise UserWithEmailAlreadyExistsException(f"AcademicCoordinator with email {academic_coordinator.email} already exists.")

        user = User.objects.create(
            username=academic_coordinator.email,
            password=academic_coordinator.id_card,
            user_type='academic_coordinator'
        )

        academic_coordinator.user = user
        self.repository.save(academic_coordinator)
        return academic_coordinator


class GetAcademicCoordinator:
    def __init__(self, repository: AcademicCoordinatorRepository):
        self.repository = repository

    def execute(self, academic_coordinator_id: int) -> AcademicCoordinator:
        academic_coordinator = self.repository.get_by_id(academic_coordinator_id)
        if not academic_coordinator:
            raise ResourceNotFoundException(f"AcademicCoordinator with id {academic_coordinator_id} not found.")
        return academic_coordinator


class UpdateAcademicCoordinator:
    def __init__(self, repository: AcademicCoordinatorRepository):
        self.repository = repository

    def execute(self, academic_coordinator_id: int, first_name: str, last_name: str, email: str) -> AcademicCoordinator:
        academic_coordinator = self.repository.get_by_id(academic_coordinator_id)
        if not AcademicCoordinator:
            raise ResourceNotFoundException(f"AcademicCoordinator with id {academic_coordinator_id} not found.")

        academic_coordinator.first_name = first_name
        academic_coordinator.first_lastname = last_name
        academic_coordinator.email = email
        self.repository.save(academic_coordinator)
        return academic_coordinator


class DeleteAcademicCoordinator:
    def __init__(self, repository: AcademicCoordinatorRepository):
        self.repository = repository

    def execute(self, academic_coordinator_id: int) -> AcademicCoordinator:
        academic_coordinator = self.repository.get_by_id(academic_coordinator_id)
        if not academic_coordinator:
            raise ResourceNotFoundException(f"AcademicCoordinator with id {academic_coordinator_id} not found.")

        self.repository.delete(academic_coordinator_id)
        return academic_coordinator


class GetAllAcademicCoordinators:
    def __init__(self, repository: AcademicCoordinatorRepository):
        self.repository = repository

    def execute(self) -> list[AcademicCoordinator]:
        coordinators = self.repository.get_all()
        if not coordinators:
            raise ResourceNotFoundException("No academics coordinators found.")
        return coordinators