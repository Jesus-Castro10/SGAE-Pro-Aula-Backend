from dependency_injector.wiring import Provide
from rest_framework.response import Response
from rest_framework.views import APIView

from sgae_app.application.services.director_service import DirectorService
from sgae_app.infrastructure.config.container import Container
from sgae_app.interfaces.dtos.director_dto import DirectorDTO
from sgae_app.domain.entities.director import Director

from rest_framework import status

class DirectorView(APIView):
    def __init__(
        self,
        director_service: DirectorService = Provide[Container.director_service],
        **kwargs
    ):
        super().__init__(**kwargs)
        self.director_service = director_service

    def post(self, request):
        dto = DirectorDTO(request.data)
        serialized = dto.data
        director = Director(**serialized)

        created = self.director_service.create_director(director)
        return Response(DirectorDTO(created).data, status=status.HTTP_201_CREATED)

    def get(self, request, director_id=None):
        if director_id:
            director = self.director_service.get_director(director_id)
            return Response(DirectorDTO(director).data)
        else:
            directors = self.director_service.get_all_directors()
            return Response(DirectorDTO(directors, many=True).data)