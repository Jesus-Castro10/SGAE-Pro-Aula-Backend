from django.db import models

class ScheduleItemModel(models.Model):
    schedule = models.ForeignKey(
        'ScheduleModel',
        on_delete=models.CASCADE,
        related_name='items'
    )
    
    subject_assignment = models.ForeignKey(
        'SubjectAssignmentModel',
        on_delete=models.CASCADE,
        related_name='schedules'
    )
    
    day_of_week = models.CharField(
        max_length=9,
        choices=[
            ('monday', 'Lunes'),
            ('tuesday', 'Martes'),
            ('wednesday', 'Miércoles'),
            ('thursday', 'Jueves'),
            ('friday', 'Viernes'),
            ('saturday', 'Sábado'),
            ('sunday', 'Domingo'),
        ]
    )
    start_time = models.TimeField(verbose_name='Hora de inicio')
    end_time = models.TimeField(verbose_name='Hora de fin')

    class Meta:
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'
        ordering = ['day_of_week', 'start_time']
        unique_together = ('subject_assignment', 'day_of_week', 'start_time')

    def __str__(self):
        sa = self.subject_assignment
        return f"{sa.subject.name} - {sa.group.name} - {self.get_day_of_week_display()} {self.start_time}-{self.end_time}"
