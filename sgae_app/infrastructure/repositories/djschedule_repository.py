from typing import List, Optional
from sgae_app.domain.entities.schedule import Schedule
from sgae_app.domain.repositories.schedule_repository import ScheduleRepository
from sgae_app.infrastructure.models.schedule import ScheduleModel

class DjangoScheduleRepository(ScheduleRepository):

    def get_by_id(self, schedule_id: int) -> Optional[Schedule]:
        try:
            return ScheduleModel.objects.get(id=schedule_id).to_domain()
        except ScheduleModel.DoesNotExist:
            return None

    def get_all(self) -> List[Schedule]:
        return [m.to_domain() for m in ScheduleModel.objects.prefetch_related('items').all()]

    def save(self, schedule: Schedule) -> Schedule:
        model = ScheduleModel.from_domain(schedule)
        model.save()
        return model.to_domain()

    def update(self, schedule_id: int, schedule: Schedule) -> Schedule:
        existing = ScheduleModel.objects.get(id=schedule_id)
        updated = ScheduleModel.from_domain(schedule)
        updated.id = existing.id
        updated.save()
        return updated.to_domain()

    def exists(self, schedule: Schedule) -> bool:
        return ScheduleModel.objects.filter(id=schedule.id).exists()

    def delete(self, schedule_id: int) -> None:
        ScheduleModel.objects.filter(id=schedule_id).delete()
