from dependency_injector import containers, providers

from sgae_app.infrastructure.repositories.djschedule_item_repo import DjangoScheduleItemRepository
from sgae_app.application.use_cases.schedule_item_uses_cases import (
    CreateScheduleItem, UpdateScheduleItem, DeleteScheduleItem,
    GetScheduleItem, GetAllScheduleItems
)
from sgae_app.application.services.schedule_item_service import ScheduleItemService

class ScheduleItemContainer(containers.DeclarativeContainer):
    schedule_item_repository = providers.Callable(DjangoScheduleItemRepository)

    create_schedule_item_use_case = providers.Factory(CreateScheduleItem, repository=schedule_item_repository)
    update_schedule_item_use_case = providers.Factory(UpdateScheduleItem, repository=schedule_item_repository)
    delete_schedule_item_use_case = providers.Factory(DeleteScheduleItem, repository=schedule_item_repository)
    get_schedule_item_use_case = providers.Factory(GetScheduleItem, repository=schedule_item_repository)
    get_all_schedule_items_use_case = providers.Factory(GetAllScheduleItems, repository=schedule_item_repository)

    schedule_item_service = providers.Factory(
        ScheduleItemService,
        create_schedule_item_uc=create_schedule_item_use_case,
        update_schedule_item_uc=update_schedule_item_use_case,
        delete_schedule_item_uc=delete_schedule_item_use_case,
        get_schedule_item_uc=get_schedule_item_use_case,
        get_all_schedule_items_uc=get_all_schedule_items_use_case,
    )
