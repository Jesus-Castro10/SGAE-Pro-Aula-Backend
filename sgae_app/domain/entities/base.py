from datetime import time

class Person:
    def __init__(
        self,
        id_card: str,
        first_name: str,
        second_name: str,
        first_lastname: str,
        second_lastname: str,
        birth_date: time,
        place_of_birth: str,
        address: str,
        phone: str,
        email: str
    ):
        self.first_name = first_name
        self.second_name = second_name
        self.first_lastname = first_lastname
        self.second_lastname = second_lastname
        self.id_card = id_card
        self.birth_date = birth_date
        self.place_of_birth = place_of_birth
        self.address = address
        self.phone = phone
        self.email = email

    def __str__(self):
        return (f"Person(first_name='{self.first_name}', second_name='{self.second_name}', "
                f"first_lastname='{self.first_lastname}', second_lastname='{self.second_lastname}', "
                f"id_card='{self.id_card}', birth_date='{self.birth_date}', "
                f"place_of_birth='{self.place_of_birth}', address='{self.address}', "
                f"phone='{self.phone}', email='{self.email}')")