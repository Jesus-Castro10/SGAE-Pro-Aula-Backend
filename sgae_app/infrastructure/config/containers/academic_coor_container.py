from dependency_injector import containers, providers

from sgae_app.infrastructure.repositories.djacademic_coordi_repo import DjangoAcademicCoordinatorRepository
from sgae_app.application.use_cases.academic_coordi_uses_cases import (
    CreateAcademicCoordinator, UpdateAcademicCoordinator, DeleteAcademicCoordinator,
    GetAcademicCoordinator, GetAllAcademicCoordinators
)
from sgae_app.application.services.academic_coordi_service import AcademicCoordinatorService
from sgae_app.infrastructure.config.containers.user_creator_container import UserCreatorContainer

class AcademicCoordinatorContainer(containers.DeclarativeContainer):
    user_creator_container = providers.Container(UserCreatorContainer)

    academic_coordinator_repository = providers.Callable(DjangoAcademicCoordinatorRepository)

    create_academic_coordinator_use_case = providers.Factory(CreateAcademicCoordinator, repository=academic_coordinator_repository)
    update_academic_coordinator_use_case = providers.Factory(UpdateAcademicCoordinator, repository=academic_coordinator_repository)
    delete_academic_coordinator_use_case = providers.Factory(DeleteAcademicCoordinator, repository=academic_coordinator_repository)
    get_academic_coordinator_use_case = providers.Factory(GetAcademicCoordinator, repository=academic_coordinator_repository)
    get_all_academic_coordinators_use_case = providers.Factory(GetAllAcademicCoordinators, repository=academic_coordinator_repository)

    academic_coordinator_service = providers.Factory(
        AcademicCoordinatorService,
        create_academic_coordinator_uc=create_academic_coordinator_use_case,
        update_academic_coordinator_uc=update_academic_coordinator_use_case,
        delete_academic_coordinator_uc=delete_academic_coordinator_use_case,
        get_academic_coordinator_uc=get_academic_coordinator_use_case,
        get_all_academic_coordinators_uc=get_all_academic_coordinators_use_case,
        user_creator=user_creator_container.user_creator_service,
    )
