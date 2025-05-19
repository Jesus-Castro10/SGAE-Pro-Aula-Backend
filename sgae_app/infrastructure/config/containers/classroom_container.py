from dependency_injector import containers, providers

from sgae_app.infrastructure.repositories.djclassroom_repository import DjangoClassRoomRepository
from sgae_app.application.use_cases.classroom_uses_cases import (
    CreateClassroom, UpdateClassroom, DeleteClassroom, GetClassroom, GetAllClassrooms
)
from sgae_app.application.services.classroom_service import ClassRoomService

class ClassroomContainer(containers.DeclarativeContainer):
    classroom_repository = providers.Callable(DjangoClassRoomRepository)

    create_classroom_use_case = providers.Factory(CreateClassroom, repository=classroom_repository)
    update_classroom_use_case = providers.Factory(UpdateClassroom, repository=classroom_repository)
    delete_classroom_use_case = providers.Factory(DeleteClassroom, repository=classroom_repository)
    get_classroom_use_case = providers.Factory(GetClassroom, repository=classroom_repository)
    get_all_classrooms_use_case = providers.Factory(GetAllClassrooms, repository=classroom_repository)

    classroom_service = providers.Factory(
        ClassRoomService,
        create_classroom_uc=create_classroom_use_case,
        update_classroom_uc=update_classroom_use_case,
        delete_classroom_uc=delete_classroom_use_case,
        get_classroom_uc=get_classroom_use_case,
        get_all_classrooms_uc=get_all_classrooms_use_case,
    )
