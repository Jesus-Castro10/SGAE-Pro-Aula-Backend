from sgae_app.domain.entities.guardian import Guardian
from sgae_app.domain.entities.student import Student
from sgae_app.domain.repositories.student_repository import StudentRepository
from auth_app.models import User

from sgae_app.domain.exceptions.exceptions import (DuplicateKeyException,
    ResourceNotFoundException, UserAlreadyExistsException)
from sgae_app.infrastructure.models.guardian import GuardianModel

from sgae_app.domain.utils.mapping import mapper

class CreateStudent:
    def __init__(self, repository: StudentRepository, email_sender_service):
        self.repository = repository
        self.notifier = UserRegistrationNotifier(email_sender_service)

    def _exists(self, student: Student) -> None:
        if self.repository.get_by_id_card(student.id_card):
            student.user.delete()
            raise UserAlreadyExistsException(
                f"Student with id card {student.id_card} already exists."
            )
        
    def execute(self,student: Student) -> Student:
        self._exists(student)
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