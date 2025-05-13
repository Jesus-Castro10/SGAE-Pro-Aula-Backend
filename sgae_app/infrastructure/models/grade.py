from django.db import models
from django.utils import timezone

class GradeModel(models.Model):
    student = models.ForeignKey(
        'sgae_app.StudentModel',
        on_delete=models.CASCADE,
        related_name='grades'
    )
    subject = models.ForeignKey(
        'sgae_app.SubjectModel',
        on_delete=models.CASCADE,
        related_name='grades'
    )
    teacher = models.ForeignKey(
        'sgae_app.TeacherModel',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_grades'
    )
    subperiod = models.CharField(
        max_length=50,
        verbose_name='Subperíodo',
        blank=True,
        null=True
    )
    
    value = models.DecimalField(
        max_digits=5, 
        decimal_places=2,
        verbose_name='Nota'
    )
    
    evaluation_type = models.CharField(
        max_length=50,
        verbose_name='Tipo de evaluación',
        blank=True,
        null=True
    )
    
    observations = models.TextField(
        blank=True,
        null=True,
        verbose_name='Observaciones'
    )
    
    registered_at = models.DateTimeField(
        default=timezone.now,
        verbose_name='Fecha de registro'
    )

    class Meta:
        verbose_name = 'Calificación'
        verbose_name_plural = 'Calificaciones'
        ordering = ['-registered_at']
        unique_together = ('student', 'subject', 'subperiod', 'evaluation_type')

    def __str__(self):
        return f"{self.student.get_short_name()} - {self.subject.name}: {self.grade_value}"
