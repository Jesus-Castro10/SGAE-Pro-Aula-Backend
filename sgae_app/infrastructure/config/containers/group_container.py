from dependency_injector import containers, providers

from sgae_app.infrastructure.repositories.djgroup_repository import DjangoGroupRepository
from sgae_app.application.use_cases.group_uses_cases import (
    CreateGroup, UpdateGroup, DeleteGroup, GetGroup, GetAllGroups
)
from sgae_app.application.services.group_service import GroupService

class GroupContainer(containers.DeclarativeContainer):
    group_repository = providers.Callable(DjangoGroupRepository)

    create_group_use_case = providers.Factory(CreateGroup, repository=group_repository)
    update_group_use_case = providers.Factory(UpdateGroup, repository=group_repository)
    delete_group_use_case = providers.Factory(DeleteGroup, repository=group_repository)
    get_group_use_case = providers.Factory(GetGroup, repository=group_repository)
    get_all_groups_use_case = providers.Factory(GetAllGroups, repository=group_repository)

    group_service = providers.Factory(
        GroupService,
        create_group_uc=create_group_use_case,
        update_group_uc=update_group_use_case,
        delete_group_uc=delete_group_use_case,
        get_group_uc=get_group_use_case,
        get_all_groups_uc=get_all_groups_use_case,
    )
