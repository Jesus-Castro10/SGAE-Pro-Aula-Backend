import logging

from sgae_app.application.services.user_creator_service import UserCreatorService
from sgae_app.application.use_cases.guardian_uses_cases import *
from sgae_app.domain.entities.guardian import Guardian
from sgae_app.interfaces.external.user_notifier_interface import UserNotifierInterface

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class GuardianService:
    def __init__(self,
                 create_guardian_uc: CreateGuardian,
                 update_guardian_uc: UpdateGuardian,
                 delete_guardian_uc: DeleteGuardian,
                 get_all_guardians_uc: GetAllGuardians,
                 get_guardian_uc: GetGuardian,
                 user_creator: UserCreatorService,
                 user_notifier: UserNotifierInterface):
        
        self.create_guardian_uc = create_guardian_uc
        self.update_guardian_uc = update_guardian_uc
        self.delete_guardian_uc = delete_guardian_uc
        self.get_guardian_uc = get_guardian_uc
        self.get_all_guardians_uc = get_all_guardians_uc
        self.user_creator = user_creator
        self.user_notifier = user_notifier

    def create_guardian(self, guardian: Guardian):
        guardian.user = self.user_creator.create_user(guardian.email, guardian.id_card, 'guardian')
        saved = self.create_guardian_uc.execute(guardian)
        if saved:
            self.user_notifier.notify_user(guardian)
        return saved

    def update_guardian(self, guardian_id, guardian: Guardian):
        return self.update_guardian_uc.execute(guardian_id, guardian)

    def delete_guardian(self, guardian_id):
        return self.delete_guardian_uc.execute(guardian_id)

    def get_guardian(self, guardian_id):
        return self.get_guardian_uc.execute(guardian_id)
    
    def get_all_guardians(self):
        return self.get_all_guardians_uc.execute()