from sgae_app.domain.entities.teacher import Teacher


class TeacherRepository:
    def get_by_id(self, teacher_id: int) -> Teacher:
        raise NotImplementedError
    
    def get_all(self) -> list[Teacher]:
        raise NotImplementedError
    
    def get_by_email(self, email: str) -> Teacher:
        raise NotImplementedError
    
    def get_by_id_card(self, id_card: str) -> Teacher:
        raise NotImplementedError

    def save(self, Teacher: Teacher) -> Teacher:
        raise NotImplementedError

    def update(self, Teacher: Teacher) -> Teacher:
        raise NotImplementedError

    def delete(self, teacher_id: int) -> None:
        raise NotImplementedError

    def exists(self, email: str) -> bool:
        raise NotImplementedError