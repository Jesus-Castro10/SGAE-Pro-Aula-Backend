from sgae_app.application.use_cases.secretary_uses_cases import (
    CreateSecretary,
    UpdateSecretary,
    DeleteSecretary,
    GetAllSecretaries,
    GetSecretary)

from sgae_app.domain.entities.secretary import Secretary

class SecretaryService:
    def __init__(self,
                 create_secretary_uc: CreateSecretary,
                 update_secretary_uc: UpdateSecretary,
                 delete_secretary_uc: DeleteSecretary,
                 get_all_secretaries_uc: GetAllSecretaries,
                 get_secretary_uc: GetSecretary):
        self.create_secretary_uc = create_secretary_uc
        self.update_secretary_uc = update_secretary_uc
        self.delete_secretary_uc = delete_secretary_uc
        self.get_secretary_uc = get_secretary_uc
        self.get_all_secretaries_uc = get_all_secretaries_uc

    def create_secretary(self, secretary: Secretary):
        return self.create_secretary_uc.execute(secretary)

    def update_secretary(self, secretary_id, first_name, last_name, email):
        return self.update_secretary_uc.execute(secretary_id, first_name, last_name, email)

    def delete_secretary(self, secretary_id):
        return self.delete_secretary_uc.execute(secretary_id)

    def get_secretary(self, secretary_id):
        return self.get_secretary_uc.execute(secretary_id)

    def get_all_secretaries(self):
        return self.get_all_secretaries_uc.execute()