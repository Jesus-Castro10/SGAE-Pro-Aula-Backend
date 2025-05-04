from django.db import models
from sgae_app.domain.entities.director import Director
from auth_app.models import User
from .base import PersonModel

class DirectorModel(PersonModel):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'user_type': 'director'}
    )

    def __str__(self):
        return f"{self.first_name} {self.first_lastname} ({self.email}"

    def to_domain(self):
        return Director(**super().to_domain(), user=self.user)

    @classmethod
    def from_domain(cls, student: Director):
        instance = super().from_domain(student)
        instance.user = student.user
        return instance