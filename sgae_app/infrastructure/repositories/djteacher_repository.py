from typing import Any

from sgae_app.domain.entities.teacher import Teacher
from sgae_app.domain.repositories.teacher_repository import TeacherRepository
from sgae_app.infrastructure.models.teacher import TeacherModel


class DjangoTeacherRepository(TeacherRepository):

    def get_by_id(self, teacher_id: int) -> Any | None:
        try:
            model = TeacherModel.objects.get(id=teacher_id)
            return model.to_domain()
        except TeacherModel.DoesNotExist:
            return None
        
    def get_all(self) -> list[Teacher]:
        return [model.to_domain() for model in TeacherModel.objects.all()]
    
    def get_by_email(self, email: str) -> Teacher:
        return TeacherModel.objects.filter(email=email).first().to_domain()
    
    def get_by_id_card(self, id_card: str) -> Teacher:
        return TeacherModel.objects.filter(id_card=id_card).first().to_domain()
    
    def save(self, teacher: Teacher) -> Teacher:
        model = TeacherModel.from_domain(teacher)
        model.save()
        return teacher

    def exists(self, teacher: Teacher) -> bool:
        return TeacherModel.objects.filter(email=teacher.email).exists() or TeacherModel.objects.filter(id_card=teacher.id_card).exists()

    def delete(self, teacher_id: int) -> None:
        TeacherModel.objects.filter(id=teacher_id).delete()