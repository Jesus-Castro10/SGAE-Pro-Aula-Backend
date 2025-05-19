from sgae_app.domain.entities.guardian import Guardian

class GuardianRepository:
    def get_by_id(self, guardian_id: int) -> Guardian:
        raise NotImplementedError
    
    def get_all(self) -> list[Guardian]:
        raise NotImplementedError
    
    def get_by_email(self, email: str) -> Guardian:
        raise NotImplementedError
    
    def get_by_id_card(self, id_card: str) -> Guardian:
        raise NotImplementedError
    
    def save(self, guardian: Guardian) -> Guardian:
        raise NotImplementedError

    def delete(self, guardian_id: int) -> None:
        raise NotImplementedError