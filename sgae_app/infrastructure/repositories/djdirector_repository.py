from typing import Any

from sgae_app.domain.repositories.director_repository import DirectorRepository
from sgae_app.infrastructure.models.director import DirectorModel
from sgae_app.domain.entities.director import Director

class DjangoDirectorRepository(DirectorRepository):
    def save(self, director: Director) -> Director:
        model = DirectorModel.from_domain(director)
        model.save()
        return model.to_domain()

    def get_by_id(self, director_id: int) -> Director | None:
        try:
            model = DirectorModel.objects.get(id=director_id)
            return model.to_domain()
        except DirectorModel.DoesNotExist:
            return None

    def get_by_email(self, email: str) -> Director | None:
        try:
            model = DirectorModel.objects.get(email=email)
            return model.to_domain()
        except DirectorModel.DoesNotExist:
            return None
        
    def get_by_id_card(self, id_card: str) -> Director | None:
        try:
            model = DirectorModel.objects.get(id_card=id_card)
            return model.to_domain()
        except DirectorModel.DoesNotExist:
            return None

    def delete(self, director_id: int) -> None:
        director = DirectorModel.objects.get(id=director_id)
        director.user.delete()
        director.delete()

    def get_all(self) -> list[Director]:
        return [model.to_domain() for model in DirectorModel.objects.all()]
