from sgae_app.domain.exceptions.exceptions import DuplicateKeyException, ResourceNotFoundException
from sgae_app.domain.utils.mapping import mapper

class CreateScheduleItem:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, scheduleItem):
        if self.repository.exists(scheduleItem):
            raise DuplicateKeyException("ScheduleItem already exists.")
        return self.repository.save(scheduleItem)

class GetScheduleItem:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, id: int):
        scheduleItem = self.repository.get_by_id(id)
        if not scheduleItem:
            raise ResourceNotFoundException("ScheduleItem not found.")
        return scheduleItem

class GetAllScheduleItems:
    def __init__(self, repository):
        self.repository = repository

    def execute(self):
        scheduleItems = self.repository.get_all()
        if not scheduleItems:
            raise ResourceNotFoundException("No ScheduleItems found.")
        return scheduleItems

class UpdateScheduleItem:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, id: int, update_data):
        schedule_item_db = self.repository.get_by_id(id)
        if not schedule_item_db:
            raise ResourceNotFoundException("ScheduleItem not found.")
        mapper(schedule_item_db, update_data, ['start_time', 'end_time', 'day_of_week'])
        return self.repository.save(schedule_item_db)

class DeleteScheduleItem:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, id: int):
        if not self.repository.get_by_id(id):
            raise ResourceNotFoundException("ScheduleItem not found.")
        self.repository.delete(id)
#class GetScheduleItemsByClassroom:
#    def __init__(self, repository):
#       self.repository = repository
#
#    def execute(self, classroom_id: int):
#        return self.repository.get_by_classroom_id(classroom_id)