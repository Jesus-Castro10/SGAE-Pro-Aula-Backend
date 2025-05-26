from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from sgae_app.application.services.schedule_service import ScheduleService
from sgae_app.interfaces.dtos.schedule_dto import ScheduleDTO
from sgae_app.domain.entities.schedule import Schedule

from dependency_injector.wiring import Provide
from sgae_app.infrastructure.config.container import Container
from sgae_app.domain.exceptions.exceptions import InvalidDataException


class ScheduleView(APIView):
    def __init__(
        self,
        schedule_service: ScheduleService = Provide[Container.schedule.schedule_service],
        **kwargs
    ):
        super().__init__(**kwargs)
        self.schedule_service = schedule_service

    def post(self, request):
        data = ScheduleDTO(data=request.data)
        if not data.is_valid():
            raise InvalidDataException(data.errors)
        print(f"Data asnte {data.data}")
        schedule = Schedule(**data.data)
        schedule_saved = self.schedule_service.create(schedule)
        return Response(ScheduleDTO(schedule_saved).data, status=status.HTTP_201_CREATED)


    def get(self, pk: int) -> Schedule:
        raise NotImplementedError("Método 'get' no implementado.")

    def get_all(self):
        try:
            schedules = self.schedule_repository.get_all()
            return list(schedules)
        except Exception as e:
            return []

    def put(self, request, pk):
        data = ScheduleDTO(data=request.data)
        if not data.is_valid():
            raise InvalidDataException(data.errors)
        schedule = Schedule(**data.data)
        updated = self.schedule_service.update(pk,schedule)
        return Response(ScheduleDTO(updated).data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        self.schedule_service.delete(pk)
        return Response("Horario eliminada correctamente", status=status.HTTP_204_NO_CONTENT)
