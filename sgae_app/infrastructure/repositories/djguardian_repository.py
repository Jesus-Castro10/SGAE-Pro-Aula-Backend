from typing import List, Optional
from sgae_app.domain.entities.guardian import Guardian
from sgae_app.domain.repositories.guardian_repository import GuardianRepository
from sgae_app.infrastructure.models.guardian import GuardianModel


class DjangoGuardianRepository(GuardianRepository):

    def get_by_id(self, guardian_id: int) -> Optional[Guardian]:
        try:
            return GuardianModel.objects.prefetch_related('students').get(id=guardian_id).to_domain()
        except GuardianModel.DoesNotExist:
            return None

    def get_all(self) -> List[Guardian]:
        return [
            model.to_domain()
            for model in GuardianModel.objects.prefetch_related('students').all()
        ]

    def get_by_email(self, email: str) -> Optional[Guardian]:
        model = GuardianModel.objects.filter(email=email).first()
        return model.to_domain() if model else None

    def get_by_id_card(self, id_card: str) -> Optional[Guardian]:
        model = GuardianModel.objects.filter(id_card=id_card).first()
        return model.to_domain() if model else None

    def save(self, guardian: Guardian) -> Guardian:
        model = GuardianModel.from_domain(guardian)
        model.save()
        return model.to_domain()

    def exists(self, guardian: Guardian) -> bool:
        return GuardianModel.objects.filter(
            id_card=guardian.id_card
        ).exists() or GuardianModel.objects.filter(
            email=guardian.email
        ).exists()

    def delete(self, guardian_id: int) -> None:
        GuardianModel.objects.filter(id=guardian_id).delete()
