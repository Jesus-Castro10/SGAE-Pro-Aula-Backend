from sgae_app.domain.exceptions.exceptions import ResourceNotFoundException, UserAlreadyExistsException
from sgae_app.domain.repositories.academic_coordinator_repo import AcademicCoordinatorRepository
from sgae_app.domain.entities.academic_coordinator import AcademicCoordinator
from auth_app.models import User
from sgae_app.domain.utils.mapping import person_mapper

class CreateAcademicCoordinator:
    def __init__(self, repository: AcademicCoordinatorRepository):
        self.repository = repository

    def execute(self, academic_coordinator: AcademicCoordinator) -> AcademicCoordinator:
        if self.repository.exists(academic_coordinator.email):
            raise UserAlreadyExistsException(f"AcademicCoordinator with email {academic_coordinator.email} already exists.")

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

    def execute(self, academic_coordinator_id: int, update_data: AcademicCoordinator) -> AcademicCoordinator:
        academic_coordi_db = self.repository.get_by_id(academic_coordinator_id)
        if not academic_coordi_db:
            raise ResourceNotFoundException(f"AcademicCoordinator with id {academic_coordinator_id} not found.")

        person_mapper(academic_coordi_db, update_data)
        
        return self.repository.save(academic_coordi_db)


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