from sgae_app.application.use_cases.group_uses_cases import *
from sgae_app.domain.entities.group import Group

class GroupService:
    def __init__(self,
                 create_group_uc: CreateGroup,
                 update_group_uc: UpdateGroup,
                 delete_group_uc: DeleteGroup,
                 get_group_uc: GetGroup,
                 get_all_groups_uc: GetAllGroups):
        
        self.create_group_uc = create_group_uc
        self.update_group_uc = update_group_uc
        self.delete_group_uc = delete_group_uc
        self.get_group_uc = get_group_uc
        self.get_all_groups_uc = get_all_groups_uc

    def create(self, group: Group):
        return self.create_group_uc.execute(group)

    def update(self, group_id, group: Group):
        return self.update_group_uc.execute(group_id, group)

    def delete(self, group_id):
        return self.delete_group_uc.execute(group_id)

    def get(self, group_id):
        return self.get_group_uc.execute(group_id)

    def get_all(self):
        return self.get_all_groups_uc.execute()
