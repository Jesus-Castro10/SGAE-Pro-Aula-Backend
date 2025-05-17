from django.db import models
from sgae_app.domain.entities.classroom import Classroom

class ClassRoomModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='Nombre del aula')
    capacity = models.IntegerField(verbose_name='Capacidad')
    registered_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')

    class Meta:
        verbose_name = 'Aula'
        verbose_name_plural = 'Aulas'

    def __str__(self):
        return f"{self.id} {self.name} - {self.capacity}"
    
    def to_domain(self):
        return Classroom(id=self.id, name=self.name, capacity=self.capacity, registered_at=self.registered_at)

    @classmethod
    def from_domain(cls, classroom):
        return cls(id=classroom.id, name=classroom.name, capacity=classroom.capacity, registered_at=classroom.registered_at)