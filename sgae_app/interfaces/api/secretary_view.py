from dependency_injector.wiring import Provide

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from sgae_app.application.services.secretary_service import SecretaryService
from sgae_app.infrastructure.config.container import Container
from sgae_app.interfaces.dtos.secretary_dto import SecretaryDTO
from sgae_app.domain.entities.secretary import Secretary

class SecretaryView(APIView):
    def __init__(self,
                 secretary_service: SecretaryService = Provide[Container.secretary_service],
                 **kwargs):
        super().__init__(**kwargs)
        self.secretary_service = secretary_service

    def post(self, request):
        data = SecretaryDTO(request.data)
        serialized = data.data
        secretary = Secretary(**serialized, user=None)

        secretary_saved = self.secretary_service.create_secretary(secretary)
        return Response(SecretaryDTO(secretary_saved).data, status=status.HTTP_201_CREATED)

    def get(self, request, secretary_id=None):
        if secretary_id:
            secretary = self.secretary_service.get_secretary(secretary_id)
            return Response(SecretaryDTO(secretary).data)
        else:
            secretaries = self.secretary_service.get_all_secretaries()
            return Response(SecretaryDTO(secretaries, many=True).data)