from typing import Optional, List
from .base import Person
from datetime import date
from django.contrib.auth.models import User

class Guardian(Person):
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
        students: Optional[List["Student"]] = None
    ):
        super().__init__(id, id_card, first_name, second_name, first_lastname, second_lastname, birthdate, place_of_birth,
                         address, phone, email, user)
        self.students = students or []

    def __str__(self):
        return f"{super().__str__()} - Representa a: {len(self.students)} estudiante(s)"


    def get_all_student_names(self):
        return [s.get_full_name() for s in self.students]
