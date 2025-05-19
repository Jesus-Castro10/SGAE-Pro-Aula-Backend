from sgae_app.domain.entities.student import Student

class StudentRepository:
    def get_by_id(self, student_id: int) -> Student:
        raise NotImplementedError
    
    def get_all(self) -> list[Student]:
        raise NotImplementedError
    
    def get_by_email(self, email: str) -> Student:
        raise NotImplementedError
    
    def get_by_id_card(self, id_card: str) -> Student:
        raise NotImplementedError
    
    def save(self, student: Student) -> Student:
        raise NotImplementedError

    def delete(self, student_id: int) -> None:
        raise NotImplementedError
    