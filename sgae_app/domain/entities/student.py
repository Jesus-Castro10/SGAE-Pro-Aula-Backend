from typing import Optional, List
from .base import Person
from datetime import date
from django.contrib.auth.models import User

class Student(Person):
    def __init__(
        self,
        id: int,
        id_card: str,
        first_name: str,
        second_name: str,
        first_lastname: str,
        second_lastname: str,
        birthdate: date,
        place_of_birth: str,
        address: str,
        phone: str,
        email: str,
        user: User,
        guardian: Optional["Guardian"] = None,
        enrollment: Optional["Enrollment"] = None,
        grades: Optional[List["Grade"]] = None
    ):
        super().__init__(id, id_card, first_name, second_name, first_lastname, second_lastname, birthdate, place_of_birth,
                         address, phone, email, user)
        self.guardian = guardian
        self.enrollment = enrollment
        self.grades = grades or []

    def __str__(self):
        return f"{super().__str__()} - Usuario: {self.user.username} - Responsable: {self.guardian.get_full_name() if self.guardian else 'N/A'}"

    def average_grade(self):
        if not self.grades:
            return None
        return round(sum(g.value for g in self.grades) / len(self.grades), 2)

    def is_enrolled(self):
        return self.enrollment is not None and self.enrollment.is_active()
