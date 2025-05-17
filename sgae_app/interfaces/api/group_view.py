from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from sgae_app.application.services.group_service import GroupService
from sgae_app.interfaces.dtos.group_dto import GroupDTO
from sgae_app.domain.entities.group import Group

from dependency_injector.wiring import Provide
from sgae_app.infrastructure.config.container import Container
from sgae_app.domain.exceptions.exceptions import InvalidDataException


class GroupView(APIView):
    def __init__(
        self,
        group_service: GroupService = Provide[Container.group_service],
        **kwargs
    ):
        super().__init__(**kwargs)
        self.group_service = group_service

    def post(self, request):
        data = GroupDTO(data=request.data)
        if not data.is_valid():
            raise InvalidDataException(data.errors)
        group = Group(**data.validated_data)
        group_saved = self.group_service.create(group)
        return Response(GroupDTO(group_saved).data, status=status.HTTP_201_CREATED)

    def get(self, request, pk=None):
        if pk:
            group = self.group_service.get(pk)
            return Response(GroupDTO(group).data)
        else:
            groups = self.group_service.get_all()
            return Response(GroupDTO(groups, many=True).data)

    def put(self, request, pk):
        data = GroupDTO(data=request.data)
        if not data.is_valid():
            raise InvalidDataException(data.errors)
        group = Group(**data.validated_data)
        updated = self.group_service.update(pk,group)
        return Response(GroupDTO(updated).data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        self.group_service.delete(pk)
        return Response("Grupo eliminado correctamente", status=status.HTTP_204_NO_CONTENT)
