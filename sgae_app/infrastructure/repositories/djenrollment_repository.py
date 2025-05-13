from typing import Any

from sgae_app.domain.entities.enrollment import Enrollment
from sgae_app.domain.repositories.enrollment_repository import EnrollmentRepository
from sgae_app.infrastructure.models.enrollment import EnrollmentModel


class DjangoEnrollmentRepository(EnrollmentRepository):

    def get_by_id(self, id: int) -> Any | None:
        try:
            model = EnrollmentModel.objects.get(id=id)
            return model.to_domain()
        except EnrollmentModel.DoesNotExist:
            return None

    def get_all(self) -> list[Enrollment]:
        return [model.to_domain() for model in EnrollmentModel.objects.all()]

    def get_by_code(self, code: str) -> Enrollment:
        return EnrollmentModel.objects.filter(id=code).first().to_domain()

    def save(self, enrollment: Enrollment) -> Enrollment:
        model = EnrollmentModel.from_domain(enrollment)
        model.save()
        return enrollment

    def exists(self, enrollment: Enrollment) -> bool:
        return EnrollmentModel.objects.filter(id=enrollment.id).exists()

    def delete(self, id: int) -> None:
        EnrollmentModel.objects.filter(id=id).delete()