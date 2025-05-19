from dependency_injector import containers, providers

from sgae_app.infrastructure.repositories.djschedule_repository import DjangoScheduleRepository
from sgae_app.application.use_cases.schedule_uses_cases import (
    CreateSchedule, UpdateSchedule, DeleteSchedule, GetSchedule, GetAllSchedules
)
from sgae_app.application.services.schedule_service import ScheduleService

class ScheduleContainer(containers.DeclarativeContainer):
    schedule_repository = providers.Callable(DjangoScheduleRepository)

    create_schedule_use_case = providers.Factory(CreateSchedule, repository=schedule_repository)
    update_schedule_use_case = providers.Factory(UpdateSchedule, repository=schedule_repository)
    delete_schedule_use_case = providers.Factory(DeleteSchedule, repository=schedule_repository)
    get_schedule_use_case = providers.Factory(GetSchedule, repository=schedule_repository)
    get_all_schedules_use_case = providers.Factory(GetAllSchedules, repository=schedule_repository)

    schedule_service = providers.Factory(
        ScheduleService,
        create_schedule_uc=create_schedule_use_case,
        update_schedule_uc=update_schedule_use_case,
        delete_schedule_uc=delete_schedule_use_case,
        get_schedule_uc=get_schedule_use_case,
        get_all_schedules_uc=get_all_schedules_use_case,
    )
