from sgae_app.domain.exceptions.exceptions import DuplicateKeyException, ResourceNotFoundException
from sgae_app.domain.utils.mapping import mapper as schedule_mapper

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
        return schedules # <-- Corrección aplicada aquí.

class UpdateSchedule:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, schedule_id: int, update_data):
        schedule_db = self.repository.get_by_id(schedule_id)
        if not schedule_db:
            raise ResourceNotFoundException("Schedule not found.")
        schedule_mapper(schedule_db, update_data, ['code', 'name'])
        return self.repository.save(schedule_db)

class DeleteSchedule:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, schedule_id: int):
        if not self.repository.get_by_id(schedule_id):
            raise ResourceNotFoundException("Schedule not found.")
        self.repository.delete(schedule_id)