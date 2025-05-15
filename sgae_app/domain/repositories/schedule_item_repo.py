from sgae_app.domain.entities.schedule_item import ScheduleItem

class ScheduleItemRepository:
    def get_all(self) -> list[ScheduleItem]:
        raise NotImplementedError

    def get_by_id(self, id: int) -> ScheduleItem:
        raise NotImplementedError

    def save(self, id: ScheduleItem) -> ScheduleItem:
        raise NotImplementedError

    def update(self, id: int, scheduleItem: ScheduleItem) -> ScheduleItem:
        raise NotImplementedError

    def exists(self, scheduleItem: ScheduleItem) -> bool:
        raise NotImplementedError

    def delete(self, id: int) -> None:
        raise NotImplementedError
