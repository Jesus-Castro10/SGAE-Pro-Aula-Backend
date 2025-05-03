from sgae_app.domain.entities.academic_coordinator import AcademicCoordinator


class AcademicCoordinatorRepository:
    def get_all(self) -> list[AcademicCoordinator]:
        raise NotImplementedError

    def get_by_id(self, academic_coordinator_id: int) -> AcademicCoordinator:
        raise NotImplementedError

    def save(self, academic_coordinator: AcademicCoordinator) -> AcademicCoordinator:
        raise NotImplementedError

    def update(self, academic_coordinator: AcademicCoordinator) -> AcademicCoordinator:
        raise NotImplementedError

    def delete(self, academic_coordinator_id: int) -> None:
        raise NotImplementedError

    def exists(self, email: str) -> bool:
        raise NotImplementedError