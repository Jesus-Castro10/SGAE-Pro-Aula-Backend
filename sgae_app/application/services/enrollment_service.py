from sgae_app.application.use_cases.enrollments_uses_cases import *
from sgae_app.domain.entities.enrollment import Enrollment

class EnrollmentService:
    def __init__(self,
                 create_enrollment_uc: CreateEnrollment,
                 update_enrollment_uc: UpdateEnrollment,
                 delete_enrollment_uc: DeleteEnrollment,
                 get_enrollment_uc: GetEnrollment,
                 get_all_enrollments_uc: GetAllEnrollments,
                 get_enrollments_by_student_uc: GetEnrollmentsByStudent):

        self.create_enrollment_uc = create_enrollment_uc
        self.update_enrollment_uc = update_enrollment_uc
        self.delete_enrollment_uc = delete_enrollment_uc
        self.get_enrollment_uc = get_enrollment_uc
        self.get_all_enrollments_uc = get_all_enrollments_uc
        self.get_enrollments_by_student_uc = get_enrollments_by_student_uc

    def create(self, enrollment: Enrollment):
        return self.create_enrollment_uc.execute(enrollment)

    def update(self, enrollment_id, enrollment: Enrollment):
        return self.update_enrollment_uc.execute(enrollment_id, enrollment)

    def delete(self, enrollment_id):
        return self.delete_enrollment_uc.execute(enrollment_id)

    def get(self, enrollment_id):
        return self.get_enrollment_uc.execute(enrollment_id)

    def get_all(self):
        return self.get_all_enrollments_uc.execute()

    def get_by_student(self, student_id):
        return self.get_enrollments_by_student_uc.execute(student_id)
