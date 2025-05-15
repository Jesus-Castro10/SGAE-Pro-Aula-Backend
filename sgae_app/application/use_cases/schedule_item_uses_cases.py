from sgae_app.domain.exceptions.exceptions import DuplicateKeyException, ResourceNotFoundException

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

    def execute(self, id: int, scheduleItem):
        if not self.repository.get_by_id(id):
            raise ResourceNotFoundException("ScheduleItem not found.")
        scheduleItem.id = id
        return self.repository.update(id, scheduleItem)

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