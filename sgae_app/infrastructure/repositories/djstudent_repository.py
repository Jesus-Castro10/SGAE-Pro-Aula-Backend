from typing import List, Optional
from sgae_app.domain.entities.student import Student
from sgae_app.domain.repositories.student_repository import StudentRepository
from sgae_app.infrastructure.models.student import StudentModel


class DjangoStudentRepository(StudentRepository):

    def get_by_id(self, student_id: int) -> Optional[Student]:
        try:
            return StudentModel.objects.get(id=student_id).to_domain()
        except StudentModel.DoesNotExist:
            return None

    def get_all(self) -> List[Student]:
        return [model.to_domain() for model in StudentModel.objects.all()]

    def get_by_email(self, email: str) -> Optional[Student]:
        model = StudentModel.objects.filter(email=email).first()
        return model.to_domain() if model else None

    def get_by_id_card(self, id_card: str) -> Optional[Student]:
        model = StudentModel.objects.filter(id_card=id_card).first()
        return model.to_domain() if model else None

    def save(self, student: Student) -> Student:
        model = StudentModel.from_domain(student)
        model.save()
        return model.to_domain()

    def exists(self, student: Student) -> bool:
        return StudentModel.objects.filter(
            id_card=student.id_card
        ).exists() or StudentModel.objects.filter(
            email=student.email
        ).exists()

    def delete(self, student_id: int) -> None:
        try:
            student = StudentModel.objects.get(id=student_id)
            student.user.delete()  # Elimina también el usuario asociado
            student.delete()
        except StudentModel.DoesNotExist:
            pass
