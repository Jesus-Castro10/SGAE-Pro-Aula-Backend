from django.db import models
from django.utils import timezone
from sgae_app.domain.entities.enrollment import Enrollment

class EnrollmentModel(models.Model):
    id = models.AutoField(
        primary_key=True,
        verbose_name='ID'
    )
    student = models.ForeignKey(
        'StudentModel',
        on_delete=models.CASCADE,
        related_name='enrollments'
    )
    group = models.ForeignKey(
        'GroupModel',
        on_delete=models.CASCADE,
        related_name='enrollments'
    )
    academic_year = models.PositiveIntegerField(
        verbose_name='Año académico'
    )
    enrollment_date = models.DateField(
        default=timezone.now,
        verbose_name='Fecha de matrícula'
    )
    status = models.CharField(
        max_length=20,
        choices=[
            ('active', 'Activa'),
            ('withdrawn', 'Retirada'),
            ('graduated', 'Graduado'),
        ],
        default='active',
        verbose_name='Estado'
    )
    observations = models.TextField(
        blank=True,
        null=True,
        verbose_name='Observaciones'
    )

    class Meta:
        verbose_name = 'Matrícula'
        verbose_name_plural = 'Matrículas'
        unique_together = ('student', 'academic_year')

    def __str__(self):
        return f"({self.id}) ({self.academic_year})"

    def to_domain(self) -> dict:
        return {
            'id': self.id,
            'student': self.student,
            'group': self.group,
            'academic_year': self.academic_year,
            'enrollment_date': self.enrollment_date,
            'status': self.status,
            'observations': self.observations
        }

    @classmethod
    def from_domain(cls, enrollment: Enrollment):
        return cls(
            id=enrollment.id,
            student=enrollment.student,
            group=enrollment.group,
            academic_year=enrollment.academic_year,
            enrollment_date=enrollment.enrollment_date,
            status=enrollment.status,
            observations=enrollment.observations,
        )