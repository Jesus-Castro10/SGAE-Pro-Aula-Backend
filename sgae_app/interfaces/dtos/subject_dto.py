from rest_framework import serializers

class SubjectDTO(serializers.Serializer):
    id = serializers.IntegerField(required=False, allow_null=True)
    name = serializers.CharField(max_length=100)
    code = serializers.CharField(max_length=10)
    description = serializers.CharField(max_length=255, required=False, allow_blank=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)