from typing import Any

from sgae_app.domain.repositories.teacher_repository import TeacherRepository
from sgae_app.infrastructure.models.teacher import TeacherModel
from sgae_app.domain.entities.teacher import Teacher

class DjangoTeacherRepository(TeacherRepository):
    def save(self, teacher: Teacher) -> Teacher:
        model = TeacherModel.from_domain(teacher)
        model.save()
        return model.to_domain()

    def get_by_id(self, teacher_id: int) -> Any | None:
        try:
            model = TeacherModel.objects.get(id=teacher_id)
            return model.to_domain()
        except TeacherModel.DoesNotExist:
            return None

    def exists(self, email: str) -> bool:
        return TeacherModel.objects.filter(email=email).exists()

    def delete(self, teacher_id: int) -> None:
        teacher = TeacherModel.objects.get(id=teacher_id)
        teacher.user.delete()
        teacher.delete()

    def get_all(self) -> list[Teacher]:
        return [model.to_domain() for model in TeacherModel.objects.all()]
