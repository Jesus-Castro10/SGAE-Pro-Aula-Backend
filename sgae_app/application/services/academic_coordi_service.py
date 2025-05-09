from sgae_app.application.use_cases.academic_coordi_uses_cases import (
    CreateAcademicCoordinator,
    UpdateAcademicCoordinator,
    DeleteAcademicCoordinator,
    GetAllAcademicCoordinators,
    GetAcademicCoordinator)
from sgae_app.domain.entities.academic_coordinator import AcademicCoordinator


class AcademicCoordinatorService:
    def __init__(self,
                 create_academic_coordinator_uc: CreateAcademicCoordinator,
                 update_academic_coordinator_uc: UpdateAcademicCoordinator,
                 delete_academic_coordinator_uc: DeleteAcademicCoordinator,
                 get_all_academic_coordinators_uc: GetAllAcademicCoordinators,
                 get_academic_coordinator_uc: GetAcademicCoordinator):
        self.create_academic_coordinator_uc = create_academic_coordinator_uc
        self.update_academic_coordinator_uc = update_academic_coordinator_uc
        self.delete_academic_coordinator_uc = delete_academic_coordinator_uc
        self.get_academic_coordinator_uc = get_academic_coordinator_uc
        self.get_all_academic_coordinators_uc = get_all_academic_coordinators_uc

    def create_academic_coordinator(self, coordinator: AcademicCoordinator):
        return self.create_academic_coordinator_uc.execute(coordinator)

    def update_academic_coordinator(self, coordinator_id, first_name, last_name, email):
        return self.update_academic_coordinator_uc.execute(coordinator_id, first_name, last_name, email)

    def delete_academic_coordinator(self, coordinator_id):
        return self.delete_academic_coordinator_uc.execute(coordinator_id)

    def get_academic_coordinator(self, coordinator_id):
        return self.get_academic_coordinator_uc.execute(coordinator_id)

    def get_all_academic_coordinators(self):
        return self.get_all_academic_coordinators_uc.execute()
