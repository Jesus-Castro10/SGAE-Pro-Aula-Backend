from rest_framework import serializers
from sgae_app.domain.exceptions.exceptions import InvalidDataException
from auth_app.models import User

class PersonDTO(serializers.Serializer):
    id = serializers.IntegerField(required=False, allow_null=True)
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
    
    image = serializers.CharField(
        required=False,
        allow_blank=True,
        allow_null=True
    )
    
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), required=False, allow_null=True
    )