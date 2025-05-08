from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from sgae_app.application.services.guardian_service import GuardianService
from sgae_app.interfaces.dtos.guardian_dto import GuardianDTO
from sgae_app.domain.entities.guardian import Guardian

from dependency_injector.wiring import Provide
from sgae_app.infrastructure.config.container import Container
from sgae_app.domain.exceptions.exceptions import InvalidDataException


class GuardianView(APIView):
    def __init__(self, 
                 guardian_service : GuardianService = None,
                 **kwargs):
        super().__init__(**kwargs)
        
        self.guardian_service = guardian_service or Container().guardian_service()

    def post(self, request):
        data = GuardianDTO(data=request.data)
        if not data.is_valid():
            raise InvalidDataException(data.errors)
        serialized = data.data
        guardian = Guardian(**serialized,students=None)
        guardianSaved = self.guardian_service.create_guardian(guardian)
        return Response(GuardianDTO(guardianSaved).data, status=status.HTTP_201_CREATED)

    def get(self, request, guardian_id=None):
        if guardian_id:
            guardian = self.guardian_service.get_guardian(guardian_id)
            return Response(GuardianDTO(guardian).data)
        else:
            guardians = self.guardian_service.get_all_guardians()
            return Response(GuardianDTO(guardians, many=True).data)
        
    def put(self, request, pk):
        data = GuardianDTO(data=request.data)
        if not data.is_valid():
            raise InvalidDataException(data.errors)
        guardian = data.data
        
        updated_guardian = self.guardian_service.update_guardian(pk,guardian)
        return Response(GuardianDTO(updated_guardian).data, status=status.HTTP_200_OK)

    def delete(self, request, guardian_id):
        self.guardian_service.delete_guardian(guardian_id)
        return Response("Tutor eliminado correctamente", status=status.HTTP_204_NO_CONTENT)