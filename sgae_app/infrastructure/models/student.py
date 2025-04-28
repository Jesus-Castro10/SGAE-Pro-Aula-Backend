from django.db import models
from sgae_app.domain.entities.student import Student

class StudentModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

    def to_domain(self):
        return Student(id=self.id, first_name=self.first_name, last_name=self.last_name, email=self.email)

    @classmethod
    def from_domain(cls, student: Student):
        return cls(id=student.id, first_name=student.first_name, last_name=student.last_name, email=student.email)