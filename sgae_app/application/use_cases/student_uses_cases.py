from sgae_app.domain.entities.guardian import Guardian
from sgae_app.domain.entities.student import Student
from sgae_app.domain.repositories.student_repository import StudentRepository
from auth_app.models import User

from sgae_app.domain.exceptions.exceptions import (DuplicateKeyException,
    ResourceNotFoundException, UserAlreadyExistsException)
from sgae_app.infrastructure.models.guardian import GuardianModel


class CreateStudent:
    def __init__(self, repository: StudentRepository):
        self.repository = repository

    def execute(
        self,
        student: Student
    ) -> Student:
        if self.repository.exists(student):
            raise UserAlreadyExistsException(f"Student already exists check the id card or email.")
        
        try:
            user = User.objects.create(
                username=student.email,
                user_type='student'
            ) #Create service to create user
            user.set_password(student.id_card)
            user.save()
            student.user = user
            guardian = GuardianModel.objects.get(id=student.guardian)
            student.guardian = guardian
            self.repository.save(student)
        except Exception as e:
            user.delete()
            raise DuplicateKeyException(errors={str(e)})
        return student

class GetStudent:
    def __init__(self, repository: StudentRepository):
        self.repository = repository

    def execute(self, student_id: int):
        student = self.repository.get_by_id(student_id)
        if not student:
            raise ResourceNotFoundException(f"Student with id {student_id} not found.")
        return student


class UpdateStudent:
    def __init__(self, repository: StudentRepository):
        self.repository = repository

    def execute(self, student_id: int, student: Student):
        student_db = self.repository.get_by_id(student_id)
        
        if not student_db:
            raise ResourceNotFoundException(f"Student with id {student_id} not found.")
        student = student_db
        student.id = student_id
        self.repository.save(student)
        return student


class DeleteStudent:
    def __init__(self, repository: StudentRepository):
        self.repository = repository

    def execute(self, student_id: int):
        student = self.repository.get_by_id(student_id)
        if not student:
            raise ResourceNotFoundException(f"Student with id {student_id} not found.")

        self.repository.delete(student_id)
        return student
    
class GetAllStudents:
    def __init__(self, repository: StudentRepository):
        self.repository = repository

    def execute(self):
        students = self.repository.get_all()
        if not students:
            raise ResourceNotFoundException("No students found.")
        return students