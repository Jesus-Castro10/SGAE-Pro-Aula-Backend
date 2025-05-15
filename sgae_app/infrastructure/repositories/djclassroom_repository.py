from typing import List, Optional
from sgae_app.domain.entities.classroom import Classroom
from sgae_app.domain.repositories.classrom_repository import ClassRoomRepository
from sgae_app.infrastructure.models.classroom import ClassRoomModel

class DjangoClassRoomRepository(ClassRoomRepository):

    def get_by_id(self, classroom_id: int) -> Optional[Classroom]:
        try:
            return ClassRoomModel.objects.get(id=classroom_id).to_domain()
        except ClassRoomModel.DoesNotExist:
            return None

    def get_all(self) -> List[Classroom]:
        return [m.to_domain() for m in ClassRoomModel.objects.all()]

    def save(self, classroom: Classroom) -> Classroom:
        model = ClassRoomModel.from_domain(classroom)
        model.save()
        return model.to_domain()

    def update(self, classroom_id: int, classroom: Classroom) -> Classroom:
        existing = ClassRoomModel.objects.get(id=classroom_id)
        updated = ClassRoomModel.from_domain(classroom)
        updated.id = existing.id
        updated.save()
        return updated.to_domain()

    def exists(self, classroom: Classroom) -> bool:
        return ClassRoomModel.objects.filter(name=classroom.name).exists()

    def delete(self, classroom_id: int) -> None:
        ClassRoomModel.objects.filter(id=classroom_id).delete()
