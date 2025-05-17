from typing import List, Optional
from sgae_app.domain.entities.group import Group
from sgae_app.domain.repositories.group_repository import GroupRepository
from sgae_app.infrastructure.models.group import GroupModel

class DjangoGroupRepository(GroupRepository):
    
    def get_by_id(self, group_id: int) -> Optional[Group]:
        try:
            return GroupModel.objects.select_related('schedule').get(id=group_id).to_domain()
        except GroupModel.DoesNotExist:
            return None

    def get_all(self) -> List[Group]:
        return [m.to_domain() for m in GroupModel.objects.select_related('schedule').all()]

    def save(self, group: Group) -> Group:
        model = GroupModel.from_domain(group)
        model.save()
        return model.to_domain()

    def exists(self, group: Group) -> bool:
        return GroupModel.objects.filter(name=group.name, year=group.year, section=group.section).exists()

    def delete(self, group_id: int) -> None:
        GroupModel.objects.filter(id=group_id).delete()
