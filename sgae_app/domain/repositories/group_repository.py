from sgae_app.domain.entities.group import Group

class GroupRepository:
    def get_all(self) -> list[Group]:
        raise NotImplementedError

    def get_by_id(self, group_id: int) -> Group:
        raise NotImplementedError

    def save(self, group: Group) -> Group:
        raise NotImplementedError

    def update(self, group_id: int, group: Group) -> Group:
        raise NotImplementedError

    def exists(self, group: Group) -> bool:
        raise NotImplementedError

    def delete(self, group_id: int) -> None:
        raise NotImplementedError
