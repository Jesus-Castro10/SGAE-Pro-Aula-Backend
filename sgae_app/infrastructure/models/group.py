from django.db import models

class GroupModel(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre del grupo')
    year = models.IntegerField(verbose_name='Año')
    section = models.CharField(max_length=10, verbose_name='Sección', blank=True, null=True)
    shift = models.CharField(max_length=10, verbose_name='Turno', blank=True, null=True)
    registered_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')
    schedule = models.ForeignKey(
        'ScheduleModel',
        on_delete=models.CASCADE,
        related_name='groups',
        verbose_name='Horario'
    )
    class Meta:
        verbose_name = 'Grupo'
        verbose_name_plural = 'Grupos'
        ordering = ['year', 'name']
        unique_together = ('name', 'year', 'section')

    def __str__(self):
        return f"{self.name} - {self.year} {self.section}"