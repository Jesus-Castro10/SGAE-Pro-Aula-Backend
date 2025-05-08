from dataclasses import dataclass, field
from typing import List, Optional
from datetime import time

from .base import Person
from django.contrib.auth.models import User

@dataclass
class Guardian(Person):
    students: Optional[List["Student"]] = field(default_factory=list)

    def __init__(self,id: int, id_card: str, first_name: str, second_name: str, first_lastname: str, second_lastname: str,
                 birthdate: time, place_of_birth: str, address: str, phone: str, email: str, user: User, students: Optional[List["Student"]]
                 ):
        super().__init__(id, id_card, first_name, second_name, first_lastname, second_lastname, birthdate, place_of_birth,
                         address, phone, email, user)
        self.students = students

    def __str__(self):
        student_names = ', '.join(str(s) for s in self.students) if self.students else 'sin estudiantes'
        return super().__str__() + f" - Students: {student_names}"