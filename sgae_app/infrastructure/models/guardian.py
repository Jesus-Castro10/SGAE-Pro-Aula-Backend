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
        student_names = ', '.join(
            f"{s.first_name} {s.first_lastname}" for s in self.students.all()
        ) or "sin estudiantes"
        return f"{self.first_name} {self.first_lastname} ({self.email}) - Estudiantes: {student_names}"

    def to_domain(self):
        students = list(self.students.all())
        base_data = super().to_domain()
        return Guardian(**base_data, user=self.user, students=students)

    @classmethod
    def from_domain(cls, guardian: Guardian):
        print("DEBUG guardian.user =", guardian.user, "TYPE =", type(guardian.user))
        instance = super().from_domain(guardian)
        instance.user = guardian.user
        return instance
