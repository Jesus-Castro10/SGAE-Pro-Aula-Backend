from django.db import models
from django.utils import timezone
from sgae_app.domain.entities.enrollment import Enrollment
from sgae_app.infrastructure.models.student import StudentModel
from sgae_app.infrastructure.models.group import GroupModel

class EnrollmentModel(models.Model):
    id = models.AutoField(
        primary_key=True,
        verbose_name='ID'
    )

    student = models.OneToOneField(
        'StudentModel',
        on_delete=models.CASCADE,
        related_name='enrollment'
    )

    group = models.ForeignKey(
        'GroupModel',
        on_delete=models.CASCADE,
        related_name='enrollments'
    )

    academic_year = models.PositiveIntegerField(verbose_name='Año académico')

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

    def to_domain(self) -> Enrollment:
        return Enrollment(
            id=self.id,
            student=self.student,
            group=self.group,
            academic_year=self.academic_year,
            enrollment_date=self.enrollment_date,
            status=self.status,
            observations=self.observations
        )

@classmethod
def from_domain(cls, enrollment: Enrollment):
    student_instance = StudentModel.objects.get(id=enrollment.student)
    group_instance = GroupModel.objects.get(id=enrollment.group)

    if enrollment.id:
        try:
            model_instance = cls.objects.get(id=enrollment.id)
            model_instance.student = student_instance
            model_instance.group = group_instance
            model_instance.academic_year = enrollment.academic_year
            model_instance.enrollment_date = enrollment.enrollment_date
            model_instance.status = enrollment.status
            model_instance.observations = enrollment.observations
            return model_instance
        except cls.DoesNotExist:
            pass
    
    return cls(
        student=student_instance,
        group=group_instance,
        academic_year=enrollment.academic_year,
        enrollment_date=enrollment.enrollment_date,
        status=enrollment.status,
        observations=enrollment.observations,
    )