from typing import List, Optional
from sgae_app.domain.entities.schedule_item import ScheduleItem
from sgae_app.domain.repositories.schedule_item_repo import ScheduleItemRepository
from sgae_app.infrastructure.models.schedule_item import ScheduleItemModel

class DjangoScheduleItemRepository(ScheduleItemRepository):

    def get_by_id(self, scheduleItem_id: int) -> Optional[ScheduleItem]:
        try:
            return ScheduleItemModel.objects.select_related('subject_assignment', 'schedule').get(id=scheduleItem_id).to_domain()
        except ScheduleItemModel.DoesNotExist:
            return None

    def get_all(self) -> List[ScheduleItem]:
        return [
            m.to_domain()
            for m in ScheduleItemModel.objects.select_related('schedule', 'subject_assignment').all()
        ]

    def get_by_teacher(self, teacher_id: int) -> List[ScheduleItem]:
        return [
            m.to_domain()
            for m in ScheduleItemModel.objects.filter(teacher_id=teacher_id).select_related('subject', 'group', 'classroom')
        ]

    def save(self, scheduleItem: ScheduleItem) -> ScheduleItem:
        print(f"Saving schedule item: {scheduleItem}")
        model = ScheduleItemModel.from_domain(scheduleItem)
        model.save()
        return model.to_domain()

    def exists(self, scheduleItem: ScheduleItem) -> bool:
        return ScheduleItemModel.objects.filter(
            id=scheduleItem.id
        ).exists()

    def delete(self, scheduleItem_id: int) -> None:
        ScheduleItemModel.objects.filter(id=scheduleItem_id).delete()
