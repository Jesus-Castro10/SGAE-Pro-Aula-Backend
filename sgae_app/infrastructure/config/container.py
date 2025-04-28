from dependency_injector import containers, providers
from sgae_app.infrastructure.repositories.djstudent_repository import DjangoStudentRepository
from sgae_app.domain.repositories.student_repository import StudentRepository
from sgae_app.application.services.student_service import StudentService
from sgae_app.domain.use_cases.student import CreateStudent, UpdateStudent, DeleteStudent, GetStudent
from sgae_app.interfaces.api.student_view import StudentView


class Container(containers.DeclarativeContainer):
    student_repository = providers.Singleton(DjangoStudentRepository)

    create_student_use_case = providers.Factory(CreateStudent, repository=student_repository)
    update_student_use_case = providers.Factory(UpdateStudent, repository=student_repository)
    delete_student_use_case = providers.Factory(DeleteStudent, repository=student_repository)
    get_student_use_case = providers.Factory(GetStudent, repository=student_repository)

    student_service = providers.Factory(
        StudentService,
        repository=student_repository,
        create_student=create_student_use_case,
        update_student=update_student_use_case,
        delete_student=delete_student_use_case,
        get_student=get_student_use_case
    )

    student_view = providers.Factory(
        StudentView,
        student_service=student_service
    )
