from sgae_app.domain.entities.director import Director


class DirectorRepository:
    def get_all(self) -> list[Director]:
        raise NotImplementedError

    def get_by_id(self, director_id: int) -> Director:
        raise NotImplementedError

    def save(self, director: Director) -> Director:
        raise NotImplementedError

    def update(self, director: Director) -> Director:
        raise NotImplementedError

    def delete(self, director_id: int) -> None:
        raise NotImplementedError

    def exists(self, email: str) -> bool:
        raise NotImplementedError