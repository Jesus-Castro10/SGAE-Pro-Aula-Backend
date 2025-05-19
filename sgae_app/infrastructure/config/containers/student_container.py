from dependency_injector import containers, providers

from sgae_app.infrastructure.repositories.djstudent_repository import DjangoStudentRepository
from sgae_app.application.use_cases.student_uses_cases import (
    CreateStudent, UpdateStudent, DeleteStudent, GetStudent, GetAllStudents
)
from sgae_app.application.services.student_service import StudentService
from sgae_app.infrastructure.config.containers.user_creator_container import UserCreatorContainer
from sgae_app.infrastructure.config.containers.email_container import EmailContainer

class StudentContainer(containers.DeclarativeContainer):
    user_creator_container = providers.Container(UserCreatorContainer)
    email_sender_container = providers.Container(EmailContainer)

    student_repository = providers.Callable(DjangoStudentRepository)

    create_student_use_case = providers.Factory(CreateStudent, repository=student_repository)
    update_student_use_case = providers.Factory(UpdateStudent, repository=student_repository)
    delete_student_use_case = providers.Factory(DeleteStudent, repository=student_repository)
    get_student_use_case = providers.Factory(GetStudent, repository=student_repository)
    get_all_students_use_case = providers.Factory(GetAllStudents, repository=student_repository)

    student_service = providers.Factory(
        StudentService,
        create_student_uc=create_student_use_case,
        update_student_uc=update_student_use_case,
        delete_student_uc=delete_student_use_case,
        get_student_uc=get_student_use_case,
        get_all_students_uc=get_all_students_use_case,
        user_creator=user_creator_container.user_creator_service,
        user_notifier=email_sender_container.user_notifier,
    )
