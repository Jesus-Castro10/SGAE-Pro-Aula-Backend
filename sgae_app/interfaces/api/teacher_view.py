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
                 teacher_service : TeacherService = None,
                 **kwargs):
        super().__init__(**kwargs)
        
        self.teacher_service = teacher_service or Container().teacher_service()

    def post(self, request):
        data = TeacherDTO(data=request.data)
        if not data.is_valid():
            raise InvalidDataException(data.errors)
        serialized = data.data
        teacher = Teacher(**serialized, user = None)
        teacherSaved = self.teacher_service.create_teacher(teacher)
        return Response(TeacherDTO(teacherSaved).data, status=status.HTTP_201_CREATED)

    def get(self, request, teacher_id=None):
        if teacher_id:
            teacher = self.teacher_service.get_teacher(teacher_id)
            return Response(TeacherDTO(teacher).data)
        else:
            teachers = self.teacher_service.get_all_teachers()
            return Response(TeacherDTO(teachers, many=True).data)
        
    def put(self, request, pk):
        data = TeacherDTO(data=request.data)
        if not data.is_valid():
            raise InvalidDataException(data.errors)
        teacher = data.data
        
        # if not teacher:
        #     return Response({"detail": "Profesor no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        
        # for key, value in serialized.items():
        #     setattr(teacher, key, value)
        
        updated_teacher = self.teacher_service.update_teacher(teacher)
        return Response(TeacherDTO(updated_teacher).data, status=status.HTTP_200_OK)

    def delete(self, request, teacher_id):
        self.teacher_service.delete_teacher(teacher_id)
        return Response("Profesor eliminado correctamente", status=status.HTTP_204_NO_CONTENT)