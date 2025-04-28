from typing import Any

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from sgae_app.application.services.student_service import StudentService
from sgae_app.interfaces.dtos.student_dto import StudentDTO

class StudentView(APIView):

    def __init__(self, student_service : StudentService,**kwargs: Any):
        super().__init__(**kwargs)
        self.student_service = student_service

    def post(self, request):
        data = request.data
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']

        student = self.student_service.create_student(first_name, last_name, email)

        return Response(StudentDTO(student).to_dict(), status=status.HTTP_201_CREATED)

    def get(self, request, student_id):
        student = self.student_service.get_student(student_id)

        return Response(StudentDTO(student).to_dict(), status=status.HTTP_200_OK)