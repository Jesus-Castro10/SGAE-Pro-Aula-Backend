from sgae_app.application.use_cases.schedule_uses_cases import *
from sgae_app.domain.entities.schedule import Schedule

class ScheduleService:
    def __init__(self,
                 create_schedule_uc: CreateSchedule,
                 update_schedule_uc: UpdateSchedule,
                 delete_schedule_uc: DeleteSchedule,
                 get_schedule_uc: GetSchedule,
                 get_all_schedules_uc: GetAllSchedules):

        self.create_schedule_uc = create_schedule_uc
        self.update_schedule_uc = update_schedule_uc
        self.delete_schedule_uc = delete_schedule_uc
        self.get_schedule_uc = get_schedule_uc
        self.get_all_schedules_uc = get_all_schedules_uc

    def create(self, schedule: Schedule):
        return self.create_schedule_uc.execute(schedule)

    def update(self, schedule_id, schedule: Schedule):
        return self.update_schedule_uc.execute(schedule_id, schedule)

    def delete(self, schedule_id):
        return self.delete_schedule_uc.execute(schedule_id)

    def get(self, schedule_id):
        return self.get_schedule_uc.execute(schedule_id)

    def get_all(self):
        return self.get_all_schedules_uc.execute()
