from typing import Any

from sgae_app.domain.repositories.director_repository import DirectorRepository
from sgae_app.infrastructure.models.director import DirectorModel
from sgae_app.domain.entities.director import Director

class DjangoDirectorRepository(DirectorRepository):
    def save(self, director: Director) -> Director:
        model = DirectorModel.from_domain(director)
        model.save()
        return director

    def get_by_id(self, director_id: int) -> Any | None:
        try:
            model = DirectorModel.objects.get(id=director_id)
            return model.to_domain()
        except DirectorModel.DoesNotExist:
            return None

    def exists(self, email: str) -> bool:
        return DirectorModel.objects.filter(email=email).exists()

    def delete(self, director_id: int) -> None:
        DirectorModel.objects.filter(id=director_id).delete()

    def get_all(self) -> list[Director]:
        return [model.to_domain() for model in DirectorModel.objects.all()]
