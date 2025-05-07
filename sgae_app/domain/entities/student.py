from .base import Person
from typing import Optional
from datetime import time

from .guardian import Guardian
from django.contrib.auth.models import User

class Student(Person):

    guardian: Optional["Guardian"] = None

    def __init__(self, id_card: str, first_name: str, second_name: str, first_lastname: str, second_lastname: str,
                 birthdate: time, place_of_birth: str, address: str, phone: str, email: str, user: User,
                 guardian: Optional[Guardian]):
        super().__init__(id_card, first_name, second_name, first_lastname, second_lastname, birthdate, place_of_birth,
                         address, phone, email, user)
        self.guardian = guardian

    def __str__(self):
        return super().__str__()