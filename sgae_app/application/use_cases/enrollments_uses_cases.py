from sgae_app.domain.exceptions.exceptions import ResourceNotFoundException
from sgae_app.domain.repositories.enrollment_repository import EnrollmentRepository
from sgae_app.domain.entities.enrollment import Enrollment
from sgae_app.infrastructure.models.student import StudentModel
from sgae_app.infrastructure.models.group import GroupModel

class CreateEnrollment:
    def __init__(self, repository: EnrollmentRepository):
        self.repository = repository

    def execute(self, enrollment: Enrollment) -> Enrollment:
        if self.repository.exists(enrollment):
            raise ResourceNotFoundException(f"Enrollment with code {enrollment.code} already exists.")
        
        student = StudentModel.objects.get(id=enrollment.student)
        group = GroupModel.objects.get(id=enrollment.group)
        enrollment.student = student
        enrollment.group = group
        self.repository.save(enrollment)
        return enrollment


class GetEnrollment:
    def __init__(self, repository: EnrollmentRepository):
        self.repository = repository

    def execute(self, Enrollment_id: int) -> Enrollment:
        enrollment = self.repository.get_by_id(Enrollment_id)
        if not enrollment:
            raise ResourceNotFoundException(f"Enrollment with id {Enrollment_id} not found.")
        return enrollment


class UpdateEnrollment:
    def __init__(self, repository: EnrollmentRepository):
        self.repository = repository

    def execute(self, enrollment_id: int, name: str, code: str, description: str = "") -> Enrollment:
        enrollment = self.repository.get_by_id(enrollment_id)
        if not enrollment:
            raise ResourceNotFoundException(f"Enrollment with id {enrollment_id} not found.")

        # Enrollment.name = name
        # Enrollment.code = code
        # Enrollment.description = description
        self.repository.save(enrollment)
        return enrollment


class DeleteEnrollment:
    def __init__(self, repository: EnrollmentRepository):
        self.repository = repository

    def execute(self, enrollment_id: int) -> Enrollment:
        Enrollment = self.repository.get_by_id(enrollment_id)
        if not Enrollment:
            raise ResourceNotFoundException(f"Enrollment with id {enrollment_id} not found.")

        self.repository.delete(enrollment_id)
        return Enrollment


class GetAllEnrollments:
    def __init__(self, repository: EnrollmentRepository):
        self.repository = repository

    def execute(self) -> list[Enrollment]:
        enrollments = self.repository.get_all()
        if not enrollments:
            raise ResourceNotFoundException("No Enrollments found.")
        return enrollments
