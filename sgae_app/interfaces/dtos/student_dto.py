from rest_framework import serializers

class StudentDTO(serializers.Serializer):
    id_card = serializers.CharField(
        max_length=20,
        min_length=5,
        required=True
    )
    
    first_name = serializers.CharField(max_length=100)
    
    second_name = serializers.CharField(
        max_length=100,
        required=False,
        allow_blank=True,
        allow_null=True
    )
    
    first_lastname = serializers.CharField(max_length=100)
    
    second_lastname = serializers.CharField(
        max_length=100,
        required=False,
        allow_blank=True,
        allow_null=True
    )
    
    birthdate = serializers.DateField()
    
    place_of_birth = serializers.CharField(max_length=100)
    
    address = serializers.CharField(max_length=255)
    
    phone = serializers.CharField(
        max_length=20,
        min_length=7
    )
    
    email = serializers.EmailField()