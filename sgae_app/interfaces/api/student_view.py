from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from sgae_app.application.services.student_service import StudentService
from sgae_app.interfaces.dtos.student_dto import StudentDTO

from dependency_injector.wiring import Provide
from sgae_app.infrastructure.config.container import Container


class StudentView(APIView):
    def __init__(self, 
                 student_service : StudentService = Provide[Container.student_service],
                 **kwargs):
        super().__init__(**kwargs)
        self.student_service = student_service

    def post(self, request):
        data = StudentDTO(request.data)
        # data.is_valid(raise_exception=True)
        serialized_data = data.data
        student = self.student_service.create_student(
            **serialized_data
        )
        return Response(serialized_data, status=status.HTTP_201_CREATED)

    def get(self, request):
        student = self.student_service.get_student(student_id=1)
        return Response(student.first_lastname, status=status.HTTP_200_OK)