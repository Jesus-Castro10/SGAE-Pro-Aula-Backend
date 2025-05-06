from django.db import models
from sgae_app.domain.entities.guardian import Guardian
from auth_app.models import User
from .base import PersonModel


class GuardianModel(PersonModel):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'user_type': 'guardian'}
    )

    def __str__(self):
        return f"{self.first_name} {self.first_lastname} ({self.email})"

    def to_domain(self):
        return Guardian(**super().to_domain(), user=self.user)

    @classmethod
    def from_domain(cls, guardian: Guardian):
        instance = super().from_domain(guardian)
        instance.user = guardian.user
        return instance
