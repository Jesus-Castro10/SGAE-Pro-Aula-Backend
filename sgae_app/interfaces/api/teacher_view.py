from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from sgae_app.application.services.teacher_service import TeacherService
from sgae_app.interfaces.dtos.teacher_dto import TeacherDTO
from sgae_app.domain.entities.teacher import Teacher

from dependency_injector.wiring import Provide
from sgae_app.infrastructure.config.container import Container
from sgae_app.domain.exceptions.exceptions import InvalidDataException


class TeacherView(APIView):
    def __init__(self, 
                 teacher_service: TeacherService = Provide[Container.teacher.teacher_service],
                 **kwargs):
        super().__init__(**kwargs)
        
        self.teacher_service = teacher_service

    def post(self, request):
        data = TeacherDTO(data=request.data)
        if not data.is_valid():
            raise InvalidDataException(data.errors)
        serialized = data.data
        teacher = Teacher(**serialized)
        teacher_saved = self.teacher_service.create_teacher(teacher)
        return Response(TeacherDTO(teacher_saved).data, status=status.HTTP_201_CREATED)

    def get(self, request, pk=None):
        if pk:
            teacher = self.teacher_service.get_teacher(pk)
            return Response(TeacherDTO(teacher).data)
        else:
            teachers = self.teacher_service.get_all_teachers()
            return Response(TeacherDTO(teachers, many=True).data)

    def put(self, request, pk):
        data = TeacherDTO(data=request.data)
        if not data.is_valid():
            raise InvalidDataException(data.errors)
        serialized = data.data
        teacher = Teacher(**serialized)
        updated_teacher = self.teacher_service.update_teacher(pk,teacher)
        return Response(TeacherDTO(updated_teacher).data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        self.teacher_service.delete_teacher(pk)
        return Response("Docente eliminado correctamente", status=status.HTTP_204_NO_CONTENT)