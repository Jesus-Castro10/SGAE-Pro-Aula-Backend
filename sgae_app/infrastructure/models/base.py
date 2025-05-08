from datetime import datetime

from django.db import models
from django.core.validators import EmailValidator, MinLengthValidator
from sgae_app.domain.entities.base import Person

class PersonModel(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField( max_length=100, blank=True, null=True)
    first_lastname = models.CharField(max_length=100)
    second_lastname = models.CharField(max_length=100)
    id_card = models.CharField(max_length=20, unique=True, validators=[MinLengthValidator(5)])
    birthdate = models.DateField()
    place_of_birth = models.CharField(max_length=100)
    address = models.TextField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, validators=[MinLengthValidator(7)])
    email = models.EmailField(max_length=100, unique=True, validators=[EmailValidator()])

    class Meta:
        abstract = True
        ordering = ['first_lastname', 'first_name']

    def __str__(self):
        return f"{self.first_name} {self.first_lastname} ({self.id_card})"

    def get_full_name(self):
        names = [self.first_name]
        if self.second_name:
            names.append(self.second_name)
        lastnames = [self.first_lastname]
        if self.second_lastname:
            lastnames.append(self.second_lastname)
        return f"{' '.join(names)} {' '.join(lastnames)}"

    def get_short_name(self):
        return f"{self.first_name} {self.first_lastname}"

    def to_domain(self) -> dict:
        return {
            'id_card': self.id_card,
            'first_name': self.first_name,
            'second_name': self.second_name,
            'first_lastname': self.first_lastname,
            'second_lastname': self.second_lastname,
            'email': self.email,
            'birthdate': self.birthdate,
            'place_of_birth': self.place_of_birth,
            'address': self.address,
            'phone': self.phone,
        }

    @classmethod
    def from_domain(cls, person: Person):
        return cls(
            id_card=person.id_card,
            first_name=person.first_name,
            second_name=person.second_name,
            first_lastname=person.first_lastname,
            second_lastname=person.second_lastname,
            email=person.email,
            birthdate=person.birthdate,
            place_of_birth=person.place_of_birth,
            address=person.address,
            phone=person.phone
        )