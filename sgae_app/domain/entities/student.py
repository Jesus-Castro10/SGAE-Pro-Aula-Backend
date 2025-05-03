from .base import Person

class Student(Person):

    def __str__(self):
        return f"{self.first_name} {self.first_lastname} ({self.email})"