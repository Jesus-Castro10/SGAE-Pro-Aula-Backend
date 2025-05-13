from typing import Any

from sgae_app.domain.entities.grade import Grade
from sgae_app.domain.repositories.grade_repository import GradeRepository
from sgae_app.infrastructure.models.grade import GradeModel


class DjangoGradeRepository(GradeRepository):

    def get_by_id(self, Grade_id: int) -> Any | None:
        try:
            model = GradeModel.objects.get(id=Grade_id)
            return model.to_domain()
        except GradeModel.DoesNotExist:
            return None

    def get_all(self) -> list[Grade]:
        return [model.to_domain() for model in GradeModel.objects.all()]

    def get_by_code(self, code: str) -> Grade:
        return GradeModel.objects.filter(code=code).first().to_domain()

    def save(self, Grade: Grade) -> Grade:
        model = GradeModel.from_domain(Grade)
        model.save()
        return Grade

    def exists(self, Grade: Grade) -> bool:
        return GradeModel.objects.filter(code=Grade.code).exists()

    def delete(self, Grade_id: int) -> None:
        GradeModel.objects.filter(id=Grade_id).delete()