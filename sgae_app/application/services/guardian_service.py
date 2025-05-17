from sgae_app.application.use_cases.guardian_uses_cases import *
from sgae_app.domain.entities.guardian import Guardian
from sgae_app.application.services.user_creator_service import UserCreatorService

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class GuardianService:
    def __init__(self,
                 create_guardian_uc: CreateGuardian,
                 update_guardian_uc: UpdateGuardian,
                 delete_guardian_uc: DeleteGuardian,
                 get_all_guardians_uc: GetAllGuardians,
                 get_guardian_uc: GetGuardian,
                 user_creator: UserCreatorService):
        
        self.create_guardian_uc = create_guardian_uc
        self.update_guardian_uc = update_guardian_uc
        self.delete_guardian_uc = delete_guardian_uc
        self.get_guardian_uc = get_guardian_uc
        self.get_all_guardians_uc = get_all_guardians_uc

    def create_guardian(self, guardian: Guardian):
        guardian.user = self.user_creator.create_user(guardian.email, guardian.id_card, 'guardian')
        return self.create_guardian_uc.execute(guardian)

    def update_guardian(self, guardian_id, guardian: Guardian):
        return self.update_guardian_uc.execute(guardian_id, guardian)

    def delete_guardian(self, guardian_id):
        return self.delete_guardian_uc.execute(guardian_id)

    def get_guardian(self, guardian_id):
        return self.get_guardian_uc.execute(guardian_id)
    
    def get_all_guardians(self):
        return self.get_all_guardians_uc.execute()