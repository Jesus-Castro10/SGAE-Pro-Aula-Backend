from django.db import models

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
