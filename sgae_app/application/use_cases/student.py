from sgae_app.domain.entities.student import Student
from sgae_app.domain.repositories.student_repository import StudentRepository
from sgae_app.domain.exceptions.student import StudentAlreadyExistsException, StudentNotFoundException
from auth_app.models import User

class CreateStudent:
    def __init__(self, repository: StudentRepository):
        self.repository = repository

    def execute(
        self,
        student: Student
    ) -> Student:
        
        if self.repository.exists(student.email):
            raise StudentAlreadyExistsException(f"Student with email {student.email} already exists.")
        
        user = User.objects.create(
            username=student.email,
            password=student.id_card,
            user_type='student'
        )

        student.user = user
        
        self.repository.save(student)
        return student

class GetStudent:
    def __init__(self, repository: StudentRepository):
        self.repository = repository

    def execute(self, student_id: int):
        student = self.repository.get_by_id(student_id)
        if not student:
            raise StudentNotFoundException(f"Student with id {student_id} not found.")
        return student


class UpdateStudent:
    def __init__(self, repository: StudentRepository):
        self.repository = repository

    def execute(self, student_id: int, first_name: str, last_name: str, email: str):
        student = self.repository.get_by_id(student_id)
        if not student:
            raise StudentNotFoundException(f"Student with id {student_id} not found.")

        student.first_name = first_name
        student.first_lastname = last_name
        student.email = email
        self.repository.save(student)
        return student


class DeleteStudent:
    def __init__(self, repository: StudentRepository):
        self.repository = repository

    def execute(self, student_id: int):
        student = self.repository.get_by_id(student_id)
        if not student:
            raise StudentNotFoundException(f"Student with id {student_id} not found.")

        self.repository.delete(student_id)
        return student
    
class GetAllStudents:
    def __init__(self, repository: StudentRepository):
        self.repository = repository

    def execute(self):
        students = self.repository.get_all()
        if not students:
            raise StudentNotFoundException("No students found.")
        return students