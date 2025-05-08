from typing import Any

from sgae_app.domain.entities.student import Student
from sgae_app.domain.repositories.student_repository import StudentRepository
from sgae_app.infrastructure.models.student import StudentModel


class DjangoStudentRepository(StudentRepository):

    def get_by_id(self, student_id: int) -> Student | None:
        try:
            model = StudentModel.objects.get(id=student_id)
            return model.to_domain()
        except StudentModel.DoesNotExist:
            return None
        
    def get_all(self) -> list[Student]:
        return [model.to_domain() for model in StudentModel.objects.all()]
    
    def get_by_email(self, email: str) -> Student:
        return StudentModel.objects.filter(email=email).first().to_domain()
    
    def get_by_id_card(self, id_card: str) -> Student:
        return StudentModel.objects.filter(id_card=id_card).first().to_domain()
    
    def save(self, student: Student) -> Student:
        model = StudentModel.from_domain(student)
        model.save()
        return student

    def exists(self, student: Student) -> bool:
        return StudentModel.objects.filter(email=student.email).exists() or StudentModel.objects.filter(id_card=student.id_card).exists()

    def delete(self, student_id: int) -> None:
        student = StudentModel.objects.get(id=student_id)
        student.user.delete()
        