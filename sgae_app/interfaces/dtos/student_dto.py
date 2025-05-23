from rest_framework import serializers

from sgae_app.interfaces.dtos.base import PersonDTO
from sgae_app.infrastructure.models.guardian import GuardianModel
from sgae_app.infrastructure.models.enrollment import EnrollmentModel
from sgae_app.interfaces.dtos.guardian_dto import GuardianDTO
from sgae_app.interfaces.dtos.response_dto import serialize


class StudentDTO(PersonDTO):
    guardian = serializers.PrimaryKeyRelatedField(
        queryset=GuardianModel.objects.all(), required=False, allow_null=True
    )
    
    enrollment = serializers.PrimaryKeyRelatedField(
        queryset=EnrollmentModel.objects.all(), required=False, allow_null=True
    )