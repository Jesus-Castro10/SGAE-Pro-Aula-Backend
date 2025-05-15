from sgae_app.domain.entities.enrollment import Enrollment

class EnrollmentRepository:
    def get_all(self) -> list[Enrollment]:
        raise NotImplementedError

    def get_by_id(self, enrollment_id: int) -> Enrollment:
        raise NotImplementedError

    def get_by_student_id(self, student_id: int) -> list[Enrollment]:
        raise NotImplementedError

    def save(self, enrollment: Enrollment) -> Enrollment:
        raise NotImplementedError

    def update(self, enrollment_id: int, enrollment: Enrollment) -> Enrollment:
        raise NotImplementedError

    def exists(self, enrollment: Enrollment) -> bool:
        raise NotImplementedError

    def delete(self, enrollment_id: int) -> None:
        raise NotImplementedError
