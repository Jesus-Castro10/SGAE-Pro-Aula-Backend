from dependency_injector import containers, providers

from sgae_app.infrastructure.repositories.djguardian_repository import DjangoGuardianRepository
from sgae_app.application.use_cases.guardian_uses_cases import (
    CreateGuardian, UpdateGuardian, DeleteGuardian, GetGuardian, GetAllGuardians
)
from sgae_app.application.services.guardian_service import GuardianService
from sgae_app.infrastructure.config.containers.user_creator_container import UserCreatorContainer

class GuardianContainer(containers.DeclarativeContainer):
    user_creator_container = providers.Container(UserCreatorContainer)

    guardian_repository = providers.Callable(DjangoGuardianRepository)

    create_guardian_use_case = providers.Factory(CreateGuardian, repository=guardian_repository)
    update_guardian_use_case = providers.Factory(UpdateGuardian, repository=guardian_repository)
    delete_guardian_use_case = providers.Factory(DeleteGuardian, repository=guardian_repository)
    get_guardian_use_case = providers.Factory(GetGuardian, repository=guardian_repository)
    get_all_guardians_use_case = providers.Factory(GetAllGuardians, repository=guardian_repository)

    guardian_service = providers.Factory(
        GuardianService,
        create_guardian_uc=create_guardian_use_case,
        update_guardian_uc=update_guardian_use_case,
        delete_guardian_uc=delete_guardian_use_case,
        get_guardian_uc=get_guardian_use_case,
        get_all_guardians_uc=get_all_guardians_use_case,
        user_creator=user_creator_container.user_creator_service,
    )
