from rest_framework import serializers

class ScheduleDTO(serializers.Serializer):
    id = serializers.IntegerField(required=False, allow_null=True)
    code = serializers.CharField(max_length=10)
    name = serializers.CharField(max_length=100)
    items = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='id'
    )