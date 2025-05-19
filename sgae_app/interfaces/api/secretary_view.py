from dependency_injector.wiring import Provide

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from sgae_app.application.services.secretary_service import SecretaryService
from sgae_app.infrastructure.config.container import Container
from sgae_app.interfaces.dtos.secretary_dto import SecretaryDTO
from sgae_app.domain.entities.secretary import Secretary
from sgae_app.domain.exceptions.exceptions import InvalidDataException

class SecretaryView(APIView):
    def __init__(self,
                 secretary_service: SecretaryService = Provide[Container.secretary.secretary_service],
                 **kwargs):
        super().__init__(**kwargs)
        self.secretary_service = secretary_service

    def post(self, request):
        data = SecretaryDTO(request.data)
        serialized = data.data
        secretary = Secretary(**serialized)

        secretary_saved = self.secretary_service.create_secretary(secretary)
        return Response(SecretaryDTO(secretary_saved).data, status=status.HTTP_201_CREATED)

    def get(self, request, pk=None):
        if pk:
            secretary = self.secretary_service.get_secretary(pk)
            return Response(SecretaryDTO(secretary).data)
        else:
            secretaries = self.secretary_service.get_all_secretaries()
            return Response(SecretaryDTO(secretaries, many=True).data)
        
    def put(self, request, pk):
        data = SecretaryDTO(data=request.data)
        if not data.is_valid():
            raise InvalidDataException(data.errors)
        serialized = data.data
        secretary = Secretary(**serialized)
        
        updated_student = self.secretary_service.update_secretary(pk,secretary)
        return Response(SecretaryDTO(updated_student).data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        self.secretary_service.delete_secretary(pk)
        return Response("Secretaria eliminado correctamente", status=status.HTTP_204_NO_CONTENT)