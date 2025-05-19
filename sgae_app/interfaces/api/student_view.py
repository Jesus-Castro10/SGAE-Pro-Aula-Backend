from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from sgae_app.application.services.student_service import StudentService
from sgae_app.interfaces.dtos.student_dto import StudentDTO
from sgae_app.domain.entities.student import Student

from dependency_injector.wiring import Provide
from sgae_app.infrastructure.config.container import Container
from sgae_app.domain.exceptions.exceptions import InvalidDataException
from sgae_app.interfaces.dtos.response_dto import serialize


class StudentView(APIView):
    def __init__(self, 
                 student_service : StudentService = Provide[Container.student_service],
                 **kwargs):
        super().__init__(**kwargs)
        
        self.student_service = student_service

    def post(self, request):
        data = StudentDTO(data=request.data)
        if not data.is_valid():
            raise InvalidDataException(data.errors)
        serialized = data.validated_data
        print(f"Serialized data: {serialized}")
        student = Student(**serialized)
        print(f"Student: {student}")
        studentSaved = self.student_service.create_student(student)
        return Response(StudentDTO(studentSaved).data, status=status.HTTP_201_CREATED)

    def get(self, request, pk=None):
        if pk:
            student = self.student_service.get_student(pk)
            return Response(StudentDTO(student).data)
        else:
            students = self.student_service.get_all_students()
            return Response(StudentDTO(students, many=True).data)
        
    def put(self, request, pk):
        data = StudentDTO(data=request.data)
        if not data.is_valid():
            raise InvalidDataException(data.errors)
        serialized = data.data
        student = Student(**serialized)
        
        updated_student = self.student_service.update_student(pk,student)
        return Response(StudentDTO(updated_student).data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        self.student_service.delete_student(pk)
        return Response("Estudiante eliminado correctamente", status=status.HTTP_204_NO_CONTENT)