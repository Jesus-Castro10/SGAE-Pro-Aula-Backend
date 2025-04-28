from sgae_app.domain.entities.student import Student

class StudentRepository:
    def save(self, student: Student) -> Student:
        raise NotImplementedError

    def get_by_id(self, student_id: int) -> Student:
        raise NotImplementedError

    def exists(self, email: str) -> bool:
        raise NotImplementedError

    def delete(self, student_id: int) -> None:
        raise NotImplementedError