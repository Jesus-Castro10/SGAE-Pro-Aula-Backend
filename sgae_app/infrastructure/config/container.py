from dependency_injector import containers, providers

from sgae_app.application.services.academic_coordi_service import AcademicCoordinatorService
from sgae_app.application.services.secretary_service import SecretaryService
from sgae_app.application.use_cases.academic_coordi_uses_cases import CreateAcademicCoordinator, \
    UpdateAcademicCoordinator, DeleteAcademicCoordinator, GetAcademicCoordinator, GetAllAcademicCoordinators
from sgae_app.application.use_cases.secretary_uses_cases import CreateSecretary, UpdateSecretary, DeleteSecretary, \
    GetSecretary, GetAllSecretaries
from sgae_app.infrastructure.repositories.djacademic_coordi_repo import DjangoAcademicCoordinatorRepository
from sgae_app.infrastructure.repositories.djsecretary_repository import DjangoSecretaryRepository
from sgae_app.infrastructure.repositories.djstudent_repository import DjangoStudentRepository
from sgae_app.application.services.student_service import StudentService
from sgae_app.application.use_cases.student_uses_cases import *


class Container(containers.DeclarativeContainer):

    config = providers.Configuration()

    # Student Dependencies
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
    )

    # Secretary Dependencies
    secretary_repository = providers.Callable(DjangoSecretaryRepository)

    create_secretary_use_case = providers.Factory(CreateSecretary, repository=secretary_repository)
    update_secretary_use_case = providers.Factory(UpdateSecretary, repository=secretary_repository)
    delete_secretary_use_case = providers.Factory(DeleteSecretary, repository=secretary_repository)
    get_secretary_use_case = providers.Factory(GetSecretary, repository=secretary_repository)
    get_all_secretaries_use_case = providers.Factory(GetAllSecretaries, repository=secretary_repository)

    secretary_service = providers.Factory(
        SecretaryService,
        create_secretary_uc=create_secretary_use_case,
        update_secretary_uc=update_secretary_use_case,
        delete_secretary_uc=delete_secretary_use_case,
        get_secretary_uc=get_secretary_use_case,
        get_all_secretaries_uc=get_all_secretaries_use_case,
    )

    #Academic Coordinator Dependencies
    academic_coordinator_repository = providers.Callable(DjangoAcademicCoordinatorRepository)

    create_academic_coordinator_use_case = providers.Factory(
        CreateAcademicCoordinator, repository=academic_coordinator_repository
    )
    update_academic_coordinator_use_case = providers.Factory(
        UpdateAcademicCoordinator, repository=academic_coordinator_repository
    )
    delete_academic_coordinator_use_case = providers.Factory(
        DeleteAcademicCoordinator, repository=academic_coordinator_repository
    )
    get_academic_coordinator_use_case = providers.Factory(
        GetAcademicCoordinator, repository=academic_coordinator_repository
    )
    get_all_academic_coordinators_use_case = providers.Factory(
        GetAllAcademicCoordinators, repository=academic_coordinator_repository
    )

    academic_coordinator_service = providers.Factory(
        AcademicCoordinatorService,
        create_academic_coordinator_uc=create_academic_coordinator_use_case,
        update_academic_coordinator_uc=update_academic_coordinator_use_case,
        delete_academic_coordinator_uc=delete_academic_coordinator_use_case,
        get_academic_coordinator_uc=get_academic_coordinator_use_case,
        get_all_academic_coordinators_uc=get_all_academic_coordinators_use_case,
    )
