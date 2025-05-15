from sgae_app.domain.exceptions.exceptions import DuplicateKeyException, ResourceNotFoundException

class CreateSchedule:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, schedule):
        if self.repository.exists(schedule):
            raise DuplicateKeyException("Schedule already exists.")
        return self.repository.save(schedule)

class GetSchedule:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, schedule_id: int):
        schedule = self.repository.get_by_id(schedule_id)
        if not schedule:
            raise ResourceNotFoundException("Schedule not found.")
        return schedule

class GetAllSchedules:
    def __init__(self, repository):
        self.repository = repository

    def execute(self):
        schedules = self.repository.get_all()
        if not schedules:
            raise ResourceNotFoundException("No schedules found.")
        return schedules

class UpdateSchedule:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, schedule_id: int, schedule):
        if not self.repository.get_by_id(schedule_id):
            raise ResourceNotFoundException("Schedule not found.")
        schedule.id = schedule_id
        return self.repository.update(schedule_id, schedule)

class DeleteSchedule:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, schedule_id: int):
        if not self.repository.get_by_id(schedule_id):
            raise ResourceNotFoundException("Schedule not found.")
        self.repository.delete(schedule_id)
#class GetSchedulesByClassroom:
#    def __init__(self, repository):
#       self.repository = repository
#
#    def execute(self, classroom_id: int):
#        return self.repository.get_by_classroom_id(classroom_id)