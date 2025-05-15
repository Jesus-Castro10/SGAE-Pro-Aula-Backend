from sgae_app.domain.entities.schedule import Schedule

class ScheduleRepository:
    def get_all(self) -> list[Schedule]:
        raise NotImplementedError

    def get_by_id(self, schedule_id: int) -> Schedule:
        raise NotImplementedError

    def save(self, schedule: Schedule) -> Schedule:
        raise NotImplementedError

    def update(self, schedule_id: int, schedule: Schedule) -> Schedule:
        raise NotImplementedError

    def exists(self, schedule: Schedule) -> bool:
        raise NotImplementedError

    def delete(self, schedule_id: int) -> None:
        raise NotImplementedError
