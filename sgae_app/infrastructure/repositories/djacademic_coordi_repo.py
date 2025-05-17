from typing import Any

from sgae_app.domain.repositories.academic_coordinator_repo import AcademicCoordinatorRepository
from sgae_app.infrastructure.models.academic_coordinator import AcademicCoordinatorModel
from sgae_app.domain.entities.academic_coordinator import AcademicCoordinator
from sgae_app.domain.exceptions.exceptions import UserAlreadyExistsException

class DjangoAcademicCoordinatorRepository(AcademicCoordinatorRepository):
    def save(self, academic_coordinator: AcademicCoordinator) -> AcademicCoordinator:
        model = AcademicCoordinatorModel.from_domain(academic_coordinator)
        model.save()
        return model.to_domain()

    def get_by_id(self, academic_coordinator_id: int) -> Any | None:
        try:
            model = AcademicCoordinatorModel.objects.get(id=academic_coordinator_id)
            return model.to_domain()
        except AcademicCoordinatorModel.DoesNotExist:
            return None

    def get_by_email(self, email: str) -> AcademicCoordinator | None:
        try:
            model = AcademicCoordinatorModel.objects.get(email=email)
            return model.to_domain()
        except AcademicCoordinatorModel.DoesNotExist:
            return None

    def get_by_id_card(self, id_card: str) -> AcademicCoordinator | None:
        try:
            model = AcademicCoordinatorModel.objects.get(id_card=id_card)
            return model.to_domain()
        except AcademicCoordinatorModel.DoesNotExist:
            return None

    def delete(self, academic_coordinator_id: int) -> None:
        academic_coordinator = AcademicCoordinatorModel.objects.get(id=academic_coordinator_id)
        academic_coordinator.user.delete()
        academic_coordinator.delete()

    def get_all(self) -> list[AcademicCoordinator]:
        return [model.to_domain() for model in AcademicCoordinatorModel.objects.all()]
