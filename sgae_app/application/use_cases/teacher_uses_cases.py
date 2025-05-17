from sgae_app.domain.entities.teacher import Teacher
from sgae_app.domain.repositories.teacher_repository import TeacherRepository
from auth_app.models import User

from sgae_app.domain.exceptions.exceptions import (DuplicateKeyException,
    ResourceNotFoundException, UserAlreadyExistsException)

from sgae_app.application.services.email_sender_service import EmailSenderService
from sgae_app.application.services.user_registration_notifier import UserRegistrationNotifier

class CreateTeacher:
    def __init__(self, repository: TeacherRepository, email_sender_service: EmailSenderService):
        self.repository = repository
        self.email_sender_service = email_sender_service

    def execute(
        self,
        teacher: Teacher
    ) -> Teacher:
        if self.repository.exists(teacher):
            raise UserAlreadyExistsException("Teacher already exists. Check the ID card or email.")
        
        try:
            user = User.objects.create(
                username=teacher.email,
                user_type='teacher'
            )
            user.set_password(teacher.id_card)
            user.save()
            teacher.user = user
            self.repository.save(teacher)
        except Exception as e:
            try:
                user.delete()
            except Exception:
                pass
            raise DuplicateKeyException(errors={str(e)})

        # Notificar registro de usuario (enviar correo)
        notifier = UserRegistrationNotifier(self.email_sender_service)
        notifier.notify_user(teacher)
        return teacher

class GetTeacher:
    def __init__(self, repository: TeacherRepository):
        self.repository = repository

    def execute(self, teacher_id: int):
        teacher = self.repository.get_by_id(teacher_id)
        if not teacher:
            raise ResourceNotFoundException(f"Teacher with id {teacher_id} not found.")
        return teacher


class UpdateTeacher:
    def __init__(self, repository: TeacherRepository):
        self.repository = repository

    def execute(self, teacher_id: int, teacher: Teacher):
        teacher_db = self.repository.get_by_id(teacher_id)
        if not teacher_db:
            raise ResourceNotFoundException(f"Teacher with id {teacher_id} not found.")
        
        self.repository.save(teacher)
        return teacher


class DeleteTeacher:
    def __init__(self, repository: TeacherRepository):
        self.repository = repository

    def execute(self, teacher_id: int):
        teacher = self.repository.get_by_id(teacher_id)
        if not teacher:
            raise ResourceNotFoundException(f"Teacher with id {teacher_id} not found.")

        self.repository.delete(teacher_id)
        return teacher
    
class GetAllTeachers:
    def __init__(self, repository: TeacherRepository):
        self.repository = repository

    def execute(self):
        teachers = self.repository.get_all()
        if not teachers:
            raise ResourceNotFoundException("No teachers found.")
        return teachers