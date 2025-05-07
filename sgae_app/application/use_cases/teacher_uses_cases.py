from sgae_app.domain.exceptions.exceptions import ResourceNotFoundException
from sgae_app.domain.repositories.teacher_repository import TeacherRepository
from sgae_app.domain.entities.teacher import Teacher
from auth_app.models import User

class CreateTeacher:
    def __init__(self, repository: TeacherRepository):
        self.repository = repository

    def execute(self, teacher: Teacher) -> Teacher:
        if self.repository.exists(teacher.email):
            raise ResourceNotFoundException(f"Teacher with email {teacher.email} already exists.")

        user = User.objects.create(
            username=teacher.email,
            password=teacher.id_card,
            user_type='teacher'
        )

        teacher.user = user
        self.repository.save(teacher)
        return teacher


class GetTeacher:
    def __init__(self, repository: TeacherRepository):
        self.repository = repository

    def execute(self, teacher_id: int) -> Teacher:
        Teacher = self.repository.get_by_id(teacher_id)
        if not Teacher:
            raise ResourceNotFoundException(f"Teacher with id {teacher_id} not found.")
        return Teacher


class UpdateTeacher:
    def __init__(self, repository: TeacherRepository):
        self.repository = repository

    def execute(self, teacher_id: int, first_name: str, last_name: str, email: str) -> Teacher:
        teacher = self.repository.get_by_id(teacher_id)
        if not teacher:
            raise ResourceNotFoundException(f"Teacher with id {teacher_id} not found.")

        teacher.first_name = first_name
        teacher.first_lastname = last_name
        teacher.email = email
        self.repository.save(teacher)
        return teacher


class DeleteTeacher:
    def __init__(self, repository: TeacherRepository):
        self.repository = repository

    def execute(self, teacher_id: int) -> Teacher:
        teacher = self.repository.get_by_id(teacher_id)
        if not teacher:
            raise ResourceNotFoundException(f"Teacher with id {teacher_id} not found.")

        self.repository.delete(teacher_id)
        return teacher


class GetAllTeachers:
    def __init__(self, repository: TeacherRepository):
        self.repository = repository

    def execute(self) -> list[Teacher]:
        teachers = self.repository.get_all()
        if not teachers:
            raise ResourceNotFoundException("No teachers found.")
        return teachers