from django.db import models
from sgae_app.domain.entities.subject import Subject

class SubjectModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField()

    def __str__(self):
        return f"Subject(name={self.name}, code={self.code})"

    def __repr__(self):
        return self.__str__()

    def to_domain(self):
        return Subject(id=self.id,name=self.name, code=self.code, description=self.description)

    @classmethod
    def from_domain(cls, subject):
        return cls(id=subject.id, name=subject.name, code=subject.code, description=subject.description)