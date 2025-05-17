from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from sgae_app.application.services.schedule_item_service import ScheduleItemService
from sgae_app.domain.entities.schedule_item import ScheduleItem

from dependency_injector.wiring import Provide
from sgae_app.infrastructure.config.container import Container
from sgae_app.domain.exceptions.exceptions import InvalidDataException
from sgae_app.interfaces.dtos.schedule_item_dto import ScheduleItemDTO


class ScheduleItemView(APIView):
    def __init__(
        self,
        schedule_item_service: ScheduleItemService = Provide[Container.schedule_item_service],
        **kwargs
    ):
        super().__init__(**kwargs)
        self.schedule_item_service = schedule_item_service

    def post(self, request):
        data = ScheduleItemDTO(data=request.data)
        if not data.is_valid():
            raise InvalidDataException(data.errors)
        scheduleItem = ScheduleItem(**data.validated_data)
        scheduleItem_saved = self.schedule_item_service.create(scheduleItem)
        return Response(ScheduleItemDTO(scheduleItem_saved).data, status=status.HTTP_201_CREATED)

    def get(self, request, pk=None):
        if pk:
            scheduleItem = self.schedule_item_service.get(pk)
            return Response(ScheduleItemDTO(scheduleItem).data)
        else:
            scheduleItems = self.schedule_item_service.get_all()
            return Response(ScheduleItemDTO(scheduleItems, many=True).data)

    def put(self, request, pk):
        data = ScheduleItemDTO(data=request.data)
        if not data.is_valid():
            raise InvalidDataException(data.errors)
        scheduleItem = ScheduleItem(**data.validated_data)
        updated = self.schedule_item_service.update(pk,scheduleItem)
        return Response(ScheduleItemDTO(updated).data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        self.schedule_item_service.delete(pk)
        return Response("Item de horario eliminado correctamente", status=status.HTTP_204_NO_CONTENT)
