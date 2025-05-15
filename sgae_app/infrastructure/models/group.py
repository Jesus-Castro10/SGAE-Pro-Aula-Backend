from django.db import models
from sgae_app.domain.entities.group import Group

class GroupModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='Nombre del grupo')
    year = models.IntegerField(verbose_name='Año')
    section = models.CharField(max_length=10, verbose_name='Sección', blank=True, null=True)
    shift = models.CharField(max_length=10, verbose_name='Turno', blank=True, null=True)
    registered_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')
    schedule = models.ForeignKey(
        'ScheduleModel',
        on_delete=models.CASCADE,
        related_name='groups',
        verbose_name='Horario',
        null=True,
    )
    class Meta:
        verbose_name = 'Grupo'
        verbose_name_plural = 'Grupos'
        ordering = ['year', 'name']
        unique_together = ('name', 'year', 'section')

    def __str__(self):
        return f"{self.name} - {self.year} {self.section}"
    
    def to_domain(self):
        return Group(id=self.id, name=self.name, year=self.year, section=self.section, shift=self.shift, registered_at=self.registered_at, schedule=self.schedule)

    @classmethod
    def from_domain(cls, subject):
        return cls(id=subject.id, name=subject.name, year=subject.year, section=subject.section, shift=subject.shift, registered_at=subject.registered_at, schedule=subject.schedule)