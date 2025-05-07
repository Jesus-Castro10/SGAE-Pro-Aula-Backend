from typing import Any

from sgae_app.domain.entities.guardian import Guardian
from sgae_app.domain.repositories.guardian_repository import GuardianRepository
from sgae_app.infrastructure.models.guardian import GuardianModel


class DjangoGuardianRepository(GuardianRepository):

    def get_by_id(self, guardian_id: int) -> Any | None:
        try:
            model = GuardianModel.objects.prefetch_related('students').get(id=guardian_id)
            return model.to_domain()
        except GuardianModel.DoesNotExist:
            return None
        
    def get_all(self) -> list[Guardian]:
        queryset = GuardianModel.objects.prefetch_related('students').all()
        print(queryset)
        return [model.to_domain() for model in queryset]
    
    def get_by_email(self, email: str) -> Guardian:
        return GuardianModel.objects.filter(email=email).first().to_domain()
    
    def get_by_id_card(self, id_card: str) -> Guardian:
        return GuardianModel.objects.filter(id_card=id_card).first().to_domain()
    
    def save(self, guardian: Guardian) -> Guardian:
        model = GuardianModel.from_domain(guardian)
        model.save()
        return guardian

    def exists(self, guardian: Guardian) -> bool:
        return GuardianModel.objects.filter(email=guardian.email).exists() or GuardianModel.objects.filter(id_card=guardian.id_card).exists()

    def delete(self, guardian_id: int) -> None:
        GuardianModel.objects.filter(id=guardian_id).delete()