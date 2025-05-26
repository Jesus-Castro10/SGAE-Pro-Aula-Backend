from rest_framework import serializers
from sgae_app.infrastructure.models.schedule import ScheduleModel

class GroupDTO(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    year = serializers.CharField(max_length=10)
    section = serializers.CharField(max_length=255, required=False, allow_blank=True)
    shift = serializers.CharField(max_length=255, required=False, allow_blank=True)
    registered_at = serializers.DateTimeField()
    schedule = serializers.PrimaryKeyRelatedField(queryset=ScheduleModel.objects.all(), required=False, allow_null=True)