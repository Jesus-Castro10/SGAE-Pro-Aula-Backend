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
        ordering = ['name']
        unique_together = ('name',)

    def __str__(self):
        return f"{self.name} - {self.capacity}"
    
    def to_domain(self):
        return Classroom(id=self.id, name=self.name, capacity=self.capacity, registered_at=self.registered_at)

    @classmethod
    def from_domain(cls, subject):
        return cls(id=subject.id, name=subject.name, capacity=subject.capacity, registered_at=subject.registered_at)