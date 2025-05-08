from datetime import time

from .base import Person
from django.contrib.auth.models import User

class Secretary(Person):

    def __init__(self,id: int, id_card: str, first_name: str, second_name: str, first_lastname: str, second_lastname: str,
            birthdate: time, place_of_birth: str, address: str, phone: str, email: str, user: User,
            ):
        super().__init__(id, id_card, first_name, second_name, first_lastname, second_lastname, birthdate, place_of_birth,
                    address, phone, email, user)
        
    def __str__(self):
        return super().__str__()