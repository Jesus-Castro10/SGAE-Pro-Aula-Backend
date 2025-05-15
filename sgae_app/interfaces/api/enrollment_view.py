from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from sgae_app.application.services.enrollment_service import EnrollmentService
from sgae_app.interfaces.dtos.enrollment_dto import EnrollmentDTO
from sgae_app.domain.entities.enrollment import Enrollment

from dependency_injector.wiring import Provide
from sgae_app.infrastructure.config.container import Container
from sgae_app.domain.exceptions.exceptions import InvalidDataException


class EnrollmentView(APIView):
    def __init__(
        self,
        enrollment_service: EnrollmentService = Provide[Container.enrollment_service],
        **kwargs
    ):
        super().__init__(**kwargs)
        self.enrollment_service = enrollment_service

    def post(self, request):
        data = EnrollmentDTO(data=request.data)
        if not data.is_valid():
            raise InvalidDataException(data.errors)
        enrollment = Enrollment(**data.data)
        enrollment_saved = self.enrollment_service.create_enrollment(enrollment)
        return Response(EnrollmentDTO(enrollment_saved).data, status=status.HTTP_201_CREATED)

    def get(self, request, pk=None):
        if pk:
            enrollment = self.enrollment_service.get(pk)
            return Response(EnrollmentDTO(enrollment).data)
        else:
            Enrollments = self.enrollment_service.get_all()
            return Response(EnrollmentDTO(Enrollments, many=True).data)

    def put(self, request, pk):
        data = EnrollmentDTO(data=request.data)
        if not data.is_valid():
            raise InvalidDataException(data.errors)
        updated = self.enrollment_service.update_enrollment(
            pk,
            name=data.validated_data["name"],
            code=data.validated_data["code"],
            description=data.validated_data.get("description", "")
        )
        return Response(EnrollmentDTO(updated).data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        self.enrollment_service.delete_Enrollment(pk)
        return Response("Asignatura eliminada correctamente", status=status.HTTP_204_NO_CONTENT)
