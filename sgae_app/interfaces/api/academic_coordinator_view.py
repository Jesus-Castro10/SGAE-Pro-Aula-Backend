from dependency_injector.wiring import Provide
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from sgae_app.application.services.academic_coordi_service import AcademicCoordinatorService
from sgae_app.infrastructure.config.container import Container
from sgae_app.interfaces.dtos.academic_coordinator_dto import AcademicCoordinatorDTO
from sgae_app.domain.entities.academic_coordinator import AcademicCoordinator

class AcademicCoordinatorView(APIView):
    def __init__(self,
                 academic_coordinator_service: AcademicCoordinatorService = Provide[Container.academic_coordinator_service],
                 **kwargs):
        super().__init__(**kwargs)
        self.academic_coordinator_service = academic_coordinator_service

    def post(self, request):
        data = AcademicCoordinatorDTO(request.data)
        serialized = data.data
        coordinator = AcademicCoordinator(**serialized)

        saved = self.academic_coordinator_service.create_academic_coordinator(coordinator)
        return Response(AcademicCoordinatorDTO(saved).data, status=status.HTTP_201_CREATED)

    def get(self, request, pk=None):
        if pk:
            coordinator = self.academic_coordinator_service.get_academic_coordinator(pk)
            return Response(AcademicCoordinatorDTO(coordinator).data)
        else:
            coordinators = self.academic_coordinator_service.get_all_academic_coordinators()
            return Response(AcademicCoordinatorDTO(coordinators, many=True).data)
        
    def put(self, request, pk):
        data = AcademicCoordinatorDTO(request.data)
        serialized = data.data
        coordinator = AcademicCoordinator(**serialized)

        updated = self.academic_coordinator_service.update_academic_coordinator(pk, coordinator)
        return Response(AcademicCoordinatorDTO(updated).data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        self.academic_coordinator_service.delete_academic_coordinator(pk)
        return Response("Director academico eliminado correctamente",status=status.HTTP_204_NO_CONTENT)