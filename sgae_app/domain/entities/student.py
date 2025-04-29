from .base import Person

class Student(Person):

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"