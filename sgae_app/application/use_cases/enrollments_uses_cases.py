from sgae_app.domain.exceptions.exceptions import DuplicateKeyException, ResourceNotFoundException
from sgae_app.infrastructure.models.student import StudentModel
from sgae_app.infrastructure.models.group import GroupModel

class CreateEnrollment:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, enrollment):
        if self.repository.exists(enrollment):
            raise DuplicateKeyException("Enrollment already exists.")
        
        student = StudentModel.objects.get(id=enrollment.student)
        group = GroupModel.objects.get(id=enrollment.group)
        if not group:
            raise ResourceNotFoundException("Group not found.")
        if not student:
            raise ResourceNotFoundException("Student not found.")
        enrollment.student = student
        enrollment.group = group
        return self.repository.save(enrollment)

class GetEnrollment:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, enrollment_id: int):
        enrollment = self.repository.get_by_id(enrollment_id)
        if not enrollment:
            raise ResourceNotFoundException("Enrollment not found.")
        return enrollment

class GetAllEnrollments:
    def __init__(self, repository):
        self.repository = repository

    def execute(self):
        enrollments = self.repository.get_all()
        if not enrollments:
            raise ResourceNotFoundException("No enrollments found.")
        return enrollments

class GetEnrollmentsByStudent:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, student_id: int):
        return self.repository.get_by_student_id(student_id)

class UpdateEnrollment:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, enrollment_id: int, enrollment):
        if not self.repository.get_by_id(enrollment_id):
            raise ResourceNotFoundException("Enrollment not found.")
        enrollment.id = enrollment_id
        return self.repository.update(enrollment_id, enrollment)

class DeleteEnrollment:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, enrollment_id: int):
        if not self.repository.get_by_id(enrollment_id):
            raise ResourceNotFoundException("Enrollment not found.")
        self.repository.delete(enrollment_id)
