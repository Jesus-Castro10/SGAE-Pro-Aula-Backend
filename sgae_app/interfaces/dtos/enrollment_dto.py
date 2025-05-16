from rest_framework import serializers
from sgae_app.infrastructure.models.student import StudentModel
from sgae_app.infrastructure.models.group import GroupModel

class EnrollmentDTO(serializers.Serializer):
    id = serializers.IntegerField(required=False, allow_null=True)
    student = serializers.PrimaryKeyRelatedField(queryset=StudentModel.objects.all(), required=False, allow_null=True)
    group = serializers.PrimaryKeyRelatedField(queryset=GroupModel.objects.all(), required=False, allow_null=True)
    enrollment_date = serializers.DateField()
    status = serializers.ChoiceField(choices=['active', 'inactive'], default='active')
    academic_year = serializers.IntegerField(required=False)
    observations = serializers.CharField(max_length=255, required=False, allow_blank=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)