from dependency_injector import containers, providers
from sgae_app.infrastructure.repositories.djstudent_repository import DjangoStudentRepository
from sgae_app.application.services.student_service import StudentService
from sgae_app.domain.use_cases.student import CreateStudent, UpdateStudent, DeleteStudent, GetStudent


class Container(containers.DeclarativeContainer):

    config = providers.Configuration()

    student_repository = providers.Callable(DjangoStudentRepository)

    create_student_use_case = providers.Factory(CreateStudent, repository=student_repository)
    update_student_use_case = providers.Factory(UpdateStudent, repository=student_repository)
    delete_student_use_case = providers.Factory(DeleteStudent, repository=student_repository)
    get_student_use_case = providers.Factory(GetStudent, repository=student_repository)

    student_service = providers.Factory(
        StudentService,
        create_student_uc=create_student_use_case,
        update_student_uc=update_student_use_case,
        delete_student_uc=delete_student_use_case,
        get_student_uc=get_student_use_case
    )
