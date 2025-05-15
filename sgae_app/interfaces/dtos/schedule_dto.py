from rest_framework import serializers

class ScheduleDTO(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    items = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='id'
    )