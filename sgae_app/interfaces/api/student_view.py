from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from sgae_app.application.services.student_service import StudentService
from sgae_app.interfaces.dtos.student_dto import StudentDTO
from sgae_app.domain.entities.student import Student

from dependency_injector.wiring import Provide
from sgae_app.infrastructure.config.container import Container
from sgae_app.domain.exceptions.student import StudentNotFoundException


class StudentView(APIView):
    def __init__(self, 
                 student_service : StudentService = Provide[Container.student_service],
                 **kwargs):
        super().__init__(**kwargs)
        
        self.student_service = student_service

    def post(self, request):
        data = StudentDTO(request.data)
        # data.is_valid(raise_exception=True)
        serialized = data.data
        student = Student(**serialized, user = None)
        
        studentSaved = self.student_service.create_student(student)
        return Response(studentSaved, status=status.HTTP_201_CREATED)

    def get(self, request, student_id=None):
        if student_id:
            student = self.student_service.get_student(student_id)
            return Response(StudentDTO(student).data)
        else:
            students = self.student_service.get_all_students()
            return Response(StudentDTO(students, many=True).data)