from sgae_app.domain.entities.secretary import Secretary


class SecretaryRepository:
    def get_all(self) -> list[Secretary]:
        raise NotImplementedError

    def get_by_id(self, secretary_id: int) -> Secretary:
        raise NotImplementedError

    def save(self, secretary: Secretary) -> Secretary:
        raise NotImplementedError

    def update(self, secretary: Secretary) -> Secretary:
        raise NotImplementedError

    def delete(self, secretary_id: int) -> None:
        raise NotImplementedError

    def get_by_email(self, email: str) -> Secretary:
        raise NotImplementedError
    
    def get_by_id_card(self, id_card: str) -> Secretary:
        raise NotImplementedError