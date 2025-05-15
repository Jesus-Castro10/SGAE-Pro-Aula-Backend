from typing import List, Optional
from sgae_app.domain.entities.enrollment import Enrollment
from sgae_app.domain.repositories.enrollment_repository import EnrollmentRepository
from sgae_app.infrastructure.models.enrollment import EnrollmentModel

class DjangoEnrollmentRepository(EnrollmentRepository):

    def get_by_id(self, enrollment_id: int) -> Optional[Enrollment]:
        try:
            return EnrollmentModel.objects.select_related('student', 'group').get(id=enrollment_id).to_domain()
        except EnrollmentModel.DoesNotExist:
            return None

    def get_all(self) -> List[Enrollment]:
        return [m.to_domain() for m in EnrollmentModel.objects.select_related('student', 'group').all()]

    def get_by_student_id(self, student_id: int) -> List[Enrollment]:
        return [
            m.to_domain() for m in EnrollmentModel.objects.select_related('group').filter(student_id=student_id)
        ]

    def save(self, enrollment: Enrollment) -> Enrollment:
        model = EnrollmentModel.from_domain(enrollment)
        model.save()
        return model.to_domain()

    def update(self, enrollment_id: int, enrollment: Enrollment) -> Enrollment:
        existing = EnrollmentModel.objects.get(id=enrollment_id)
        updated = EnrollmentModel.from_domain(enrollment)
        updated.id = existing.id
        updated.save()
        return updated.to_domain()

    def exists(self, enrollment: Enrollment) -> bool:
        return EnrollmentModel.objects.filter(student_id=enrollment.student.id, academic_year=enrollment.academic_year).exists()

    def delete(self, enrollment_id: int) -> None:
        EnrollmentModel.objects.filter(id=enrollment_id).delete()
