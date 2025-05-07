from django.db import models
from sgae_app.domain.entities.student import Student
from auth_app.models import User
from .base import PersonModel


class StudentModel(PersonModel):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'user_type': 'student'}
    )

    guardian = models.ForeignKey(
        'GuardianModel',
        related_name='students',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.first_name} {self.first_lastname} ({self.email})"

    def to_domain(self):
        return Student(**super().to_domain(), user=self.user, guardian=self.guardian)

    @classmethod
    def from_domain(cls, student: Student):
        instance = super().from_domain(student)
        instance.user = student.user
        instance.guardian = student.guardian
        return instance
