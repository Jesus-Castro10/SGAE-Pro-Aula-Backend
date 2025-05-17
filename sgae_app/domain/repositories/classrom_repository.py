from sgae_app.domain.entities.classroom import Classroom

class ClassRoomRepository:
    def get_all(self) -> list[Classroom]:
        raise NotImplementedError

    def get_by_id(self, classroom_id: int) -> Classroom:
        raise NotImplementedError

    def save(self, classroom: Classroom) -> Classroom:
        raise NotImplementedError

    def exists(self, classroom: Classroom) -> bool:
        raise NotImplementedError

    def delete(self, classroom_id: int) -> None:
        raise NotImplementedError
