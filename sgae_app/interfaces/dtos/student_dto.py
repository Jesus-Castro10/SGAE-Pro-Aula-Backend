from rest_framework import serializers

from sgae_app.interfaces.dtos.base import PersonDTO
from sgae_app.infrastructure.models.guardian import GuardianModel
from sgae_app.infrastructure.models.enrollment import EnrollmentModel


class StudentDTO(PersonDTO):
    guardian = serializers.PrimaryKeyRelatedField(
        queryset=GuardianModel.objects.all(), required=False, allow_null=True
    )
    
    enrollment = serializers.PrimaryKeyRelatedField(
        queryset=EnrollmentModel.objects.all(), required=False, allow_null=True
    )