from dependency_injector import containers, providers

from sgae_app.infrastructure.repositories.djenrollment_repository import DjangoEnrollmentRepository
from sgae_app.application.use_cases.enrollments_uses_cases import (
    CreateEnrollment, UpdateEnrollment, DeleteEnrollment, GetEnrollment,
    GetAllEnrollments, GetEnrollmentsByStudent
)
from sgae_app.application.services.enrollment_service import EnrollmentService

class EnrollmentContainer(containers.DeclarativeContainer):
    enrollment_repository = providers.Callable(DjangoEnrollmentRepository)

    create_enrollment_use_case = providers.Factory(CreateEnrollment, repository=enrollment_repository)
    update_enrollment_use_case = providers.Factory(UpdateEnrollment, repository=enrollment_repository)
    delete_enrollment_use_case = providers.Factory(DeleteEnrollment, repository=enrollment_repository)
    get_enrollment_use_case = providers.Factory(GetEnrollment, repository=enrollment_repository)
    get_all_enrollments_use_case = providers.Factory(GetAllEnrollments, repository=enrollment_repository)
    get_enrollments_by_student_use_case = providers.Factory(GetEnrollmentsByStudent, repository=enrollment_repository)

    enrollment_service = providers.Factory(
        EnrollmentService,
        create_enrollment_uc=create_enrollment_use_case,
        update_enrollment_uc=update_enrollment_use_case,
        delete_enrollment_uc=delete_enrollment_use_case,
        get_enrollment_uc=get_enrollment_use_case,
        get_all_enrollments_uc=get_all_enrollments_use_case,
        get_enrollments_by_student_uc=get_enrollments_by_student_use_case,
    )
