from django.db import models

class SubjectAssignmentModel(models.Model):
    teacher = models.ForeignKey(
        'TeacherModel',
        on_delete=models.CASCADE,
        related_name='subject_assignments'
    )
    subject = models.ForeignKey(
        'SubjectModel',
        on_delete=models.CASCADE,
        related_name='subject_assignments'
    )
    group = models.ForeignKey(
        'GroupModel',
        on_delete=models.CASCADE,
        related_name='subject_assignments'
    )
    academic_year = models.PositiveIntegerField(
        verbose_name='Año académico'
    )
    
    classroom = models.ForeignKey(
        'ClassRoomModel',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='subject_assignments'
    )

    class Meta:
        verbose_name = 'Asignación de materia'
        verbose_name_plural = 'Asignaciones de materias'
        unique_together = ('teacher', 'subject', 'group', 'academic_year')

    def __str__(self):
        return f"{self.teacher.get_short_name()} - {self.subject.name} - {self.group.name} ({self.academic_year})"
