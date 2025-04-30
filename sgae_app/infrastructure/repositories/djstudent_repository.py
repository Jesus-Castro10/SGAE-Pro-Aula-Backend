from typing import Any

from sgae_app.domain.entities.student import Student
from sgae_app.domain.repositories.student_repository import StudentRepository
from sgae_app.infrastructure.models.student import StudentModel

class DjangoStudentRepository(StudentRepository):
    def save(self, student: Student) -> Student:
        model = StudentModel.from_domain(student)
        model.save()
        return student

    def get_by_id(self, student_id: int) -> Any | None:
        try:
            model = StudentModel.objects.get(id=student_id)
            return model.to_domain()
        except StudentModel.DoesNotExist:
            return None

    def exists(self, email: str) -> bool:
        return StudentModel.objects.filter(email=email).exists()

    def delete(self, student_id: int) -> None:
        StudentModel.objects.filter(id=student_id).delete()
        
    def get_all(self) -> list[Student]:
        return [model.to_domain() for model in StudentModel.objects.all()]