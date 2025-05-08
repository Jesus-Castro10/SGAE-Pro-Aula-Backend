from rest_framework import serializers

from sgae_app.interfaces.dtos.base import PersonDTO
from sgae_app.domain.entities.guardian import Guardian
from sgae_app.interfaces.dtos.guardian_dto import GuardianDTO
from sgae_app.infrastructure.models.guardian import GuardianModel


class StudentDTO(PersonDTO):
    guardian = serializers.PrimaryKeyRelatedField(
        queryset=GuardianModel.objects.all(), required=False, allow_null=True
    )