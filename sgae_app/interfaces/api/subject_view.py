from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from sgae_app.application.services.subject_service import SubjectService
from sgae_app.interfaces.dtos.subject_dto import SubjectDTO
from sgae_app.domain.entities.subject import Subject

from dependency_injector.wiring import Provide
from sgae_app.infrastructure.config.container import Container
from sgae_app.domain.exceptions.exceptions import InvalidDataException


class SubjectView(APIView):
    def __init__(
        self,
        subject_service: SubjectService = Provide[Container.subject.subject_service],
        **kwargs
    ):
        super().__init__(**kwargs)
        self.subject_service = subject_service

    def post(self, request):
        data = SubjectDTO(data=request.data)
        if not data.is_valid():
            raise InvalidDataException(data.errors)
        subject = Subject(**data.validated_data)
        subject_saved = self.subject_service.create_subject(subject)
        return Response(SubjectDTO(subject_saved).data, status=status.HTTP_201_CREATED)

    def get(self, request, pk=None):
        if pk:
            subject = self.subject_service.get_subject(pk)
            return Response(SubjectDTO(subject).data)
        else:
            subjects = self.subject_service.get_all_subjects()
            return Response(SubjectDTO(subjects, many=True).data)

    def put(self, request, pk):
        data = SubjectDTO(data=request.data)
        if not data.is_valid():
            raise InvalidDataException(data.errors)
        serialized = data.data
        subject = Subject(**serialized)
        updated = self.subject_service.update_subject(pk, subject)
        return Response(SubjectDTO(updated).data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        self.subject_service.delete_subject(pk)
        return Response("Asignatura eliminada correctamente", status=status.HTTP_204_NO_CONTENT)
