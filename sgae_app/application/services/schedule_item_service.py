from sgae_app.application.use_cases.schedule_item_uses_cases import *
from sgae_app.domain.entities.schedule_item import ScheduleItem

class ScheduleItemService:
    def __init__(self,
                 create_schedule_item_uc: CreateScheduleItem,
                 update_schedule_item_uc: UpdateScheduleItem,
                 delete_schedule_item_uc: DeleteScheduleItem,
                 get_schedule_item_uc: GetScheduleItem,
                 get_all_schedule_items_uc: GetAllScheduleItems):

        self.create_schedule_item_uc = create_schedule_item_uc
        self.update_schedule_item_uc = update_schedule_item_uc
        self.delete_schedule_item_uc = delete_schedule_item_uc
        self.get_schedule_item_uc = get_schedule_item_uc
        self.get_all_schedule_items_uc = get_all_schedule_items_uc

    def create(self, scheduleItem: ScheduleItem):
        return self.create_schedule_item_uc.execute(scheduleItem)

    def update(self, id, scheduleItem: ScheduleItem):
        return self.update_schedule_item_uc.execute(id, scheduleItem)

    def delete(self, id):
        return self.delete_schedule_item_uc.execute(id)

    def get(self, id):
        return self.get_schedule_item_uc.execute(id)

    def get_all(self):
        return self.get_all_schedule_items_uc.execute()
