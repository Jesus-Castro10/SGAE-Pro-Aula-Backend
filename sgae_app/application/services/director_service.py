from sgae_app.application.services.user_creator_service import UserCreatorService
from sgae_app.application.use_cases.director_uses_cases import *
from sgae_app.domain.entities.director import Director
from sgae_app.interfaces.external.user_notifier_interface import UserNotifierInterface


class DirectorService:
    def __init__(self,
                 create_director_uc: CreateDirector,
                 update_director_uc: UpdateDirector,
                 delete_director_uc: DeleteDirector,
                 get_all_directors_uc: GetAllDirectors,
                 get_director_uc: GetDirector,
                 user_creator: UserCreatorService,
                 user_notifier: UserNotifierInterface):
        self.create_director_uc = create_director_uc
        self.update_director_uc = update_director_uc
        self.delete_director_uc = delete_director_uc
        self.get_director_uc = get_director_uc
        self.get_all_directors_uc = get_all_directors_uc
        self.user_creator = user_creator
        self.user_notifier = user_notifier

    def create_director(self, director: Director):
        director.user = self.user_creator.create_user(director.email, director.id_card, 'director')
        saved = self.create_director_uc.execute(director)
        if saved:
            self.user_notifier.notify_user(director)
        return saved

    def update_director(self, director_id, director: Director):
        return self.update_director_uc.execute(director_id, director)

    def delete_director(self, director_id):
        return self.delete_director_uc.execute(director_id)

    def get_director(self, director_id):
        return self.get_director_uc.execute(director_id)

    def get_all_directors(self):
        return self.get_all_directors_uc.execute()