from rest_framework import serializers
from sgae_app.infrastructure.models.subject_assignment import SubjectAssignmentModel
from sgae_app.infrastructure.models.schedule import ScheduleModel

class ScheduleItemDTO(serializers.Serializer):
    id = serializers.IntegerField(required=False, allow_null=True)
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
    schedule = serializers.PrimaryKeyRelatedField(queryset=ScheduleModel.objects.all())