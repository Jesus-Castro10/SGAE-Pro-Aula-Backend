from sgae_app.domain.exceptions.exceptions import ResourceNotFoundException, UserAlreadyExistsException, DuplicateKeyException
from sgae_app.domain.repositories.academic_coordinator_repo import AcademicCoordinatorRepository
from sgae_app.domain.entities.academic_coordinator import AcademicCoordinator
from auth_app.models import User
from sgae_app.domain.utils.mapping import person_mapper

class CreateAcademicCoordinator:
    def __init__(self, repository: AcademicCoordinatorRepository):
        self.repository = repository

    def _exists(self, academic_coordinator: AcademicCoordinator) -> None:
        if self.repository.get_by_id_card(academic_coordinator.id_card):
            academic_coordinator.user.delete()
            raise UserAlreadyExistsException(
                f"AcademicCoordinator with id card {academic_coordinator.id_card} already exists."
            )

    def execute(self, academic_coordinator: AcademicCoordinator) -> AcademicCoordinator:
        self._exists(academic_coordinator)
        try:
            return self.repository.save(academic_coordinator)
        except Exception as e:
            academic_coordinator.user.delete()
            raise DuplicateKeyException(f"Error creating academic creator. {str(e)}")  

    
    


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