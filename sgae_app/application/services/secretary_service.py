from sgae_app.application.services.user_creator_service import UserCreatorService
from sgae_app.application.use_cases.secretary_uses_cases import (
    CreateSecretary,
    DeleteSecretary,
    GetAllSecretaries,
    GetSecretary,
    UpdateSecretary,
)
from sgae_app.domain.entities.secretary import Secretary
from sgae_app.interfaces.external.user_notifier_interface import UserNotifierInterface


class SecretaryService:
    def __init__(self,
                 create_secretary_uc: CreateSecretary,
                 update_secretary_uc: UpdateSecretary,
                 delete_secretary_uc: DeleteSecretary,
                 get_all_secretaries_uc: GetAllSecretaries,
                 get_secretary_uc: GetSecretary,
                 user_creator: UserCreatorService,
                 user_notifier: UserNotifierInterface):
        
        self.create_secretary_uc = create_secretary_uc
        self.update_secretary_uc = update_secretary_uc
        self.delete_secretary_uc = delete_secretary_uc
        self.get_secretary_uc = get_secretary_uc
        self.get_all_secretaries_uc = get_all_secretaries_uc
        self.user_creator = user_creator
        self.user_notifier = user_notifier

    def create_secretary(self, secretary: Secretary):
        secretary.user = self.user_creator.create_user(secretary.email, secretary.id_card, 'secretary')
        saved = self.create_secretary_uc.execute(secretary)
        if saved:
            self.user_notifier.notify_user(secretary)
        return saved

    def update_secretary(self, secretary_id, secretary: Secretary):
        return self.update_secretary_uc.execute(secretary_id, secretary)

    def delete_secretary(self, secretary_id):
        return self.delete_secretary_uc.execute(secretary_id)

    def get_secretary(self, secretary_id):
        return self.get_secretary_uc.execute(secretary_id)

    def get_all_secretaries(self):
        return self.get_all_secretaries_uc.execute()