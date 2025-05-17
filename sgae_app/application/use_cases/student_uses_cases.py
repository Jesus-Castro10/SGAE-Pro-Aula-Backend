from sgae_app.domain.entities.guardian import Guardian
from sgae_app.domain.entities.student import Student
from sgae_app.domain.repositories.student_repository import StudentRepository
from auth_app.models import User

from sgae_app.domain.exceptions.exceptions import (DuplicateKeyException,
    ResourceNotFoundException, UserAlreadyExistsException)
from sgae_app.infrastructure.models.guardian import GuardianModel

from sgae_app.domain.utils.mapping import mapper

class CreateStudent:
    def __init__(self, repository: StudentRepository):
        self.repository = repository

    def execute(
        self,
        student: Student
    ) -> Student:
        if self.repository.exists(student):
            raise UserAlreadyExistsException(f"Student already exists check the id card or email.")
        return self.repository.save(student)

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

    def execute(self, student_id: int, updated_data: Student):
        existing_student = self.repository.get_by_id(student_id)
        
        if not existing_student:
            raise ResourceNotFoundException(f"Student with id {student_id} not found.")

        mapper(existing_student, updated_data, [
            'id_card', 'first_name', 'second_name', 'first_lastname', 'second_lastname',
            'birthdate', 'place_of_birth', 'address', 'phone', 'email', 'image'
        ])

        existing_student.guardian = GuardianModel.objects.get(id=updated_data.guardian)

        self.repository.save(existing_student)
        return existing_student



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