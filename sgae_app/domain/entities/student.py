from .base import Person
from typing import Optional, List
from dataclasses import field
from datetime import time

from .guardian import Guardian
from django.contrib.auth.models import User
 
class Student(Person):

    guardian: Optional["Guardian"] = None
    grades: Optional[List["Grade"]] = field(default_factory=list)
    enrollment: Optional["Enrollment"] = None

    def __init__(self,id: int, id_card: str, first_name: str, second_name: str, first_lastname: str, second_lastname: str,
                 birthdate: time, place_of_birth: str, address: str, phone: str, email: str, user: User,
                 guardian: Optional[Guardian], enrollment: Optional["Enrollment"]):
        super().__init__(id, id_card, first_name, second_name, first_lastname, second_lastname, birthdate, place_of_birth,
                         address, phone, email, user)
        self.guardian = guardian
        self.enrollment = enrollment

    def __str__(self):
        return super().__str__() + f"(user : {self.user})" + f"( guardian : {self.guardian})"