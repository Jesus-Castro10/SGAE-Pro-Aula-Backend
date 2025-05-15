from sgae_app.domain.entities.classroom import ClassRoom

class ClassRoomRepository:
    def get_all(self) -> list[ClassRoom]:
        raise NotImplementedError

    def get_by_id(self, classroom_id: int) -> ClassRoom:
        raise NotImplementedError

    def save(self, classroom: ClassRoom) -> ClassRoom:
        raise NotImplementedError

    def update(self, classroom_id: int, classroom: ClassRoom) -> ClassRoom:
        raise NotImplementedError

    def exists(self, classroom: ClassRoom) -> bool:
        raise NotImplementedError

    def delete(self, classroom_id: int) -> None:
        raise NotImplementedError
