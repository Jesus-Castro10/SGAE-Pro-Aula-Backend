from django.db import models
from sgae_app.domain.entities.schedule import Schedule

class ScheduleModel(models.Model):
    id = models.AutoField(
        primary_key=True,
        verbose_name='ID'
    )
    
    class Meta:
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'

    def __str__(self):
        return f"{self.id})"
    
    def to_domain(self):
        items = list(self.items.all())
        return Schedule(id=self.id, items=items)

    @classmethod
    def from_domain(cls, subject):
        return cls(id=subject.id, items=subject.items)
