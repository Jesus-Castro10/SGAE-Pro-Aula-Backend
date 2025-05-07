from rest_framework import serializers

from sgae_app.interfaces.dtos.base import PersonDTO
from sgae_app.interfaces.dtos.guardian_dto import GuardianDTO


class StudentDTO(PersonDTO):
    guardian = serializers.PrimaryKeyRelatedField(read_only=True)