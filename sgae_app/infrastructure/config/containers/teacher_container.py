from dependency_injector import containers, providers

from sgae_app.infrastructure.repositories.djteacher_repository import DjangoTeacherRepository
from sgae_app.application.use_cases.teacher_uses_cases import (
    CreateTeacher, UpdateTeacher, DeleteTeacher, GetTeacher, GetAllTeachers
)
from sgae_app.application.services.teacher_service import TeacherService
from sgae_app.infrastructure.config.containers.user_creator_container import UserCreatorContainer
from sgae_app.infrastructure.config.containers.email_container import EmailContainer

class TeacherContainer(containers.DeclarativeContainer):
    user_creator_container = providers.Container(UserCreatorContainer)
    email_sender_container = providers.Container(EmailContainer)

    teacher_repository = providers.Callable(DjangoTeacherRepository)

    create_teacher_use_case = providers.Factory(CreateTeacher,repository=teacher_repository)
    update_teacher_use_case = providers.Factory(UpdateTeacher, repository=teacher_repository)
    delete_teacher_use_case = providers.Factory(DeleteTeacher, repository=teacher_repository)
    get_teacher_use_case = providers.Factory(GetTeacher, repository=teacher_repository)
    get_all_teachers_use_case = providers.Factory(GetAllTeachers, repository=teacher_repository)

    teacher_service = providers.Factory(
        TeacherService,
        create_teacher_uc=create_teacher_use_case,
        update_teacher_uc=update_teacher_use_case,
        delete_teacher_uc=delete_teacher_use_case,
        get_teacher_uc=get_teacher_use_case,
        get_all_teachers_uc=get_all_teachers_use_case,
        user_creator=user_creator_container.user_creator_service,
        user_notifier=email_sender_container.user_notifier,
    )
