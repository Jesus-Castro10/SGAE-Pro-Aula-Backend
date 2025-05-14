from rest_framework import serializers
from sgae_app.interfaces.dtos.base import PersonDTO

class GuardianDTO(PersonDTO):    
    students = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='id_card'
     )