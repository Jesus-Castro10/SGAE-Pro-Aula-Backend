from sgae_app.domain.entities.student import Student
from sgae_app.domain.repositories.student_repository import StudentRepository
from sgae_app.domain.exceptions.student import StudentAlreadyExistsException, StudentNotFoundException


class CreateStudent:
    def __init__(self, repository: StudentRepository):
        self.repository = repository

    def execute(
        self,
        first_name: str,
        first_lastname: str,
        id_card: str,
        birth_date: str,
        place_of_birth: str,
        address: str,
        phone: str,
        email: str,
        second_name: str = None,
        second_lastname: str = None
    ) -> Student:
        if self.repository.exists(email):
            raise StudentAlreadyExistsException(f"Student with email {email} already exists.")

        student = Student(
            first_name=first_name,
            second_name=second_name,
            first_lastname=first_lastname,
            second_lastname=second_lastname,
            id_card=id_card,
            birth_date=birth_date,
            place_of_birth=place_of_birth,
            address=address,
            phone=phone,
            email=email
        )
        
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
        student.last_name = last_name
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
        return {"message": "Student deleted successfully"}