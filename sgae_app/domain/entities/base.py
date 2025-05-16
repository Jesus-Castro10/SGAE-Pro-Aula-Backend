from datetime import date
from django.contrib.auth.models import User
import re

class Person:
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
        image: str = None,
    ):
        if not id_card or len(id_card.strip()) < 5:
            raise ValueError("La cédula es obligatoria y debe tener al menos 5 caracteres.")
        if not first_name or not first_lastname:
            raise ValueError("El nombre y el primer apellido son obligatorios.")
        if not self._is_valid_email(email):
            raise ValueError("Email no válido.")
        if not self._is_valid_phone(phone):
            raise ValueError("Teléfono no válido (solo dígitos, min 7).")

        self.id = id
        self.id_card = id_card
        self.first_name = first_name
        self.second_name = second_name
        self.first_lastname = first_lastname
        self.second_lastname = second_lastname
        self.birthdate = birthdate
        self.place_of_birth = place_of_birth
        self.address = address
        self.phone = phone
        self.email = email
        self.user = user
        self.image = image

    def __str__(self):
        return f"{self.get_full_name()} ({self.id_card}) - {self.image or 'Sin imagen'}"

    def get_full_name(self):
        return f"{self.first_name} {self.second_name or ''} {self.first_lastname} {self.second_lastname or ''}".strip()

    def _is_valid_email(self, email: str) -> bool:
        return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

    def _is_valid_phone(self, phone: str) -> bool:
        return phone.isdigit() and len(phone) >= 7
