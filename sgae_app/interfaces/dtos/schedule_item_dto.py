from rest_framework import serializers
from sgae_app.infrastructure.models.subject_assignment import SubjectAssignmentModel

class ScheduleItemDTO(serializers.Serializer):
    id = serializers.IntegerField()
    start_time = serializers.TimeField()
    end_time = serializers.TimeField()
    day_of_week = serializers.ChoiceField(choices=[
        ('monday', 'Lunes'),
        ('tuesday', 'Martes'),
        ('wednesday', 'Miércoles'),
        ('thursday', 'Jueves'),
        ('friday', 'Viernes'),
        ('saturday', 'Sábado'),
        ('sunday', 'Domingo'),
    ])
    subject_assignment = serializers.PrimaryKeyRelatedField(queryset=SubjectAssignmentModel.objects.all())
    schedule = serializers.PrimaryKeyRelatedField(queryset=SubjectAssignmentModel.objects.all())