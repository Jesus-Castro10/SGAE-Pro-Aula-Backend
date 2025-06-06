from rest_framework import serializers

class ClassroomDTO(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(max_length=100)
    capacity = serializers.IntegerField()
    registered_at = serializers.DateTimeField()