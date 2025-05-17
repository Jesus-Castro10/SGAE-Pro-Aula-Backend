from django.db import models
from sgae_app.domain.entities.schedule_item import ScheduleItem

class ScheduleItemModel(models.Model):
    id = models.AutoField(
        primary_key=True,
    )
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

    def __str__(self):
        sa = self.subject_assignment
        return f"{sa.subject.name} - {sa.group.name} - {self.get_day_of_week_display()} {self.start_time}-{self.end_time}"
    
    def to_domain(self):
        return ScheduleItem(id=self.id, 
                            subject_assignment=self.subject_assignment,
                            day_of_week=self.day_of_week,
                            start_time=self.start_time,
                            end_time=self.end_time,
                            schedule=self.schedule)

    @classmethod
    def from_domain(cls, subject):
        return cls(id=subject.id, 
                   subject_assignment=subject.subject_assignment,
                   day_of_week=subject.day_of_week,
                   start_time=subject.start_time,
                   end_time=subject.end_time,
                   schedule=subject.schedule)
