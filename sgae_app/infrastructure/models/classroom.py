from django.db import models

class ClassRoomModel(models.Model):
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