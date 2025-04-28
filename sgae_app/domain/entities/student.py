from .base import Person

class Student(Person):
    # def __init__(self, id: int, first_name: str, last_name: str, email: str):
        

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"