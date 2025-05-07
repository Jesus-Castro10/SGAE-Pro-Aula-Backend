from typing import List, TYPE_CHECKING

from rest_framework import serializers

from sgae_app.interfaces.dtos.base import PersonDTO


class GuardianDTO(PersonDTO):
    def get_fields(self):
        fields = super().get_fields()
        from sgae_app.interfaces.dtos.student_dto import StudentDTO  # Import diferido
        fields['students'] = StudentDTO(many=True, read_only=True)
        return fields