from django.db import models
from sgae_app.domain.entities.schedule import Schedule

class ScheduleModel(models.Model):
    id = models.AutoField(
        primary_key=True,
        verbose_name='ID'
    )

    code = models.CharField(
        max_length=10,
        verbose_name='Código',
        unique=True
    )

    name = models.CharField(
        max_length=100,
        verbose_name='Nombre',
        unique=True
    )
    
    class Meta:
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'

    def __str__(self):
        return f"{self.id})"
    
    def to_domain(self):
        items = list(self.items.all())
        return Schedule(id=self.id,code=self.code,name=self.name,items=items)

    @classmethod
    def from_domain(cls, schedule):
        return cls(id=schedule.id,code=schedule.code,name=schedule.name)
