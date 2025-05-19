from dependency_injector import containers, providers

from sgae_app.infrastructure.repositories.djsecretary_repository import DjangoSecretaryRepository
from sgae_app.application.use_cases.secretary_uses_cases import (
    CreateSecretary, UpdateSecretary, DeleteSecretary, GetSecretary, GetAllSecretaries
)
from sgae_app.application.services.secretary_service import SecretaryService
from sgae_app.infrastructure.config.containers.user_creator_container import UserCreatorContainer
from sgae_app.infrastructure.config.containers.email_container import EmailContainer


class SecretaryContainer(containers.DeclarativeContainer):
    user_creator_container = providers.Container(UserCreatorContainer)
    email_sender_container = providers.Container(EmailContainer)

    secretary_repository = providers.Callable(DjangoSecretaryRepository)

    create_secretary_use_case = providers.Factory(CreateSecretary, repository=secretary_repository)
    update_secretary_use_case = providers.Factory(UpdateSecretary, repository=secretary_repository)
    delete_secretary_use_case = providers.Factory(DeleteSecretary, repository=secretary_repository)
    get_secretary_use_case = providers.Factory(GetSecretary, repository=secretary_repository)
    get_all_secretaries_use_case = providers.Factory(GetAllSecretaries, repository=secretary_repository)

    secretary_service = providers.Factory(
        SecretaryService,
        create_secretary_uc=create_secretary_use_case,
        update_secretary_uc=update_secretary_use_case,
        delete_secretary_uc=delete_secretary_use_case,
        get_secretary_uc=get_secretary_use_case,
        get_all_secretaries_uc=get_all_secretaries_use_case,
        user_creator=user_creator_container.user_creator_service,
        user_notifier=email_sender_container.user_notifier,
    )
