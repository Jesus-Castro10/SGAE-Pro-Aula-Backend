from typing import Any

from sgae_app.domain.repositories.secretary_repository import SecretaryRepository
from sgae_app.infrastructure.models.secretary import SecretaryModel
from sgae_app.domain.entities.secretary import Secretary

class DjangoSecretaryRepository(SecretaryRepository):
    def save(self, secretary: Secretary) -> Secretary:
        model = SecretaryModel.from_domain(secretary)
        model.save()
        return model.to_domain()

    def get_by_id(self, secretary_id: int) -> Any | None:
        try:
            model = SecretaryModel.objects.get(id=secretary_id)
            return model.to_domain()
        except SecretaryModel.DoesNotExist:
            return None

    def get_by_email(self, email: str) -> Secretary | None:
        try:
            model = SecretaryModel.objects.get(email=email)
            return model.to_domain()
        except SecretaryModel.DoesNotExist:
            return None
        
    def get_by_id_card(self, id_card: str) -> Secretary | None:
        try:
            model = SecretaryModel.objects.get(id_card=id_card)
            return model.to_domain()
        except SecretaryModel.DoesNotExist:
            return None

    def delete(self, secretary_id: int) -> None:
        secretary = SecretaryModel.objects.get(id=secretary_id)
        secretary.user.delete()
        secretary.delete()

    def get_all(self) -> list[Secretary]:
        return [model.to_domain() for model in SecretaryModel.objects.all()]
