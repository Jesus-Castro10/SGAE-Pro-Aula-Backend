from django.db import models
from sgae_app.domain.entities.teacher import Teacher
from auth_app.models import User
from .base import PersonModel

class TeacherModel(PersonModel):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'user_type': 'teacher'}
    )

    def __str__(self):
        return f"{self.first_name} {self.first_lastname} ({self.email}"

    def to_domain(self):
        return Teacher(**super().to_domain(), user=self.user)

    @classmethod
    def from_domain(cls, teacher: Teacher):
        instance = super().from_domain(teacher)
        instance.user = teacher.user
        return instance