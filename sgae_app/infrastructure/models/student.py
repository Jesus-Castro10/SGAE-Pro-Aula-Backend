from django.db import models
from sgae_app.domain.entities.student import Student
from auth_app.models import User
from .base import Person


class StudentModel(Person):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        limit_choices_to={'user_type': 'student'}
    )

    def __str__(self):
        return f"{self.first_name} {self.first_lastname} ({self.email})"

    def to_domain(self):
        return Student(first_name=self.first_name,second_name=self.second_name,
                        first_lastname=self.first_lastname,second_lastname=self.second_lastname, 
                        id_card=self.id_card, birthdate=self.birthdate, place_of_birth=self.place_of_birth,
                        address=self.address, phone=self.phone, email=self.email,user=self.user)

    @classmethod
    def from_domain(cls, student: Student):
        return cls(id_card=student.id_card,first_name=student.first_name,second_name=student.second_name, 
                   first_lastname=student.first_lastname,second_lastname= student.second_lastname, 
                   email=student.email, birthdate=student.birthdate,
                   place_of_birth=student.place_of_birth, address=student.address, phone=student.phone, user = student.user)