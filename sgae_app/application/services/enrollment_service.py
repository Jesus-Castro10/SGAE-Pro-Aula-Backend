from sgae_app.domain.entities.enrollment import Enrollment
from sgae_app.application.use_cases.enrollments_uses_cases import *


class EnrollmentService:
    def __init__(
        self,
        create_enrollment_uc: CreateEnrollment,
        update_enrollment_uc: UpdateEnrollment,
        delete_enrollment_uc: DeleteEnrollment,
        get_enrollment_uc: GetEnrollment,
        get_all_enrollments_uc: GetAllEnrollments,
    ):
        self.create_enrollment_uc = create_enrollment_uc
        self.update_enrollment_uc = update_enrollment_uc
        self.delete_enrollment_uc = delete_enrollment_uc
        self.get_enrollment_uc = get_enrollment_uc
        self.get_all_enrollments_uc = get_all_enrollments_uc

    def create_enrollment(self, enrollment: Enrollment) -> Enrollment:
        return self.create_enrollment_uc.execute(enrollment)

    def update_enrollment(self, enrollment_id: int, name: str, code: str, description: str = "") -> Enrollment:
        return self.update_enrollment_uc.execute(enrollment_id, name, code, description)

    def delete_enrollment(self, enrollment_id: int) -> Enrollment:
        return self.delete_enrollment_uc.execute(enrollment_id)

    def get_enrollment(self, enrollment_id: int) -> Enrollment:
        return self.get_enrollment_uc.execute(enrollment_id)

    def get_all_enrollments(self) -> list[Enrollment]:
        return self.get_all_enrollments_uc.execute()
