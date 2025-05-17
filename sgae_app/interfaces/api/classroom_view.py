from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from sgae_app.application.services.classroom_service import ClassRoomService
from sgae_app.domain.entities.classroom import Classroom

from dependency_injector.wiring import Provide
from sgae_app.infrastructure.config.container import Container
from sgae_app.domain.exceptions.exceptions import InvalidDataException
from sgae_app.interfaces.dtos.classroom_dto import ClassroomDTO


class ClassroomView(APIView):
    def __init__(
        self,
        classroom_service: ClassRoomService = Provide[Container.classroom_service],
        **kwargs
    ):
        super().__init__(**kwargs)
        self.classroom_service = classroom_service

    def post(self, request):
        data = ClassroomDTO(data=request.data)
        if not data.is_valid():
            raise InvalidDataException(data.errors)
        classroom = Classroom(**data.validated_data)
        classroom_saved = self.classroom_service.create(classroom)
        return Response(ClassroomDTO(classroom_saved).data, status=status.HTTP_201_CREATED)

    def get(self, request, pk=None):
        if pk:
            classroom = self.classroom_service.get(pk)
            return Response(ClassroomDTO(classroom).data)
        else:
            classrooms = self.classroom_service.get_all()
            return Response(ClassroomDTO(classrooms, many=True).data)

    def put(self, request, pk):
        data = ClassroomDTO(data=request.data)
        if not data.is_valid():
            raise InvalidDataException(data.errors)
        classroom = Classroom(**data.validated_data)
        updated = self.classroom_service.update(pk, classroom)
        return Response(ClassroomDTO(updated).data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        self.classroom_service.delete(pk)
        return Response("Aula eliminada correctamente", status=status.HTTP_204_NO_CONTENT)
