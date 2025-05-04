from sgae_app.application.use_cases.director_uses_cases import (
    CreateDirector,
    UpdateDirector,
    DeleteDirector,
    GetAllDirectors,
    GetDirector)
from sgae_app.domain.entities.director import Director

class DirectorService:
    def __init__(self,
                 create_director_uc: CreateDirector,
                 update_director_uc: UpdateDirector,
                 delete_director_uc: DeleteDirector,
                 get_all_directors_uc: GetAllDirectors,
                 get_director_uc: GetDirector):
        self.create_director_uc = create_director_uc
        self.update_director_uc = update_director_uc
        self.delete_director_uc = delete_director_uc
        self.get_director_uc = get_director_uc
        self.get_all_directors_uc = get_all_directors_uc

    def create_director(self, director: Director):
        return self.create_director_uc.execute(director)

    def update_director(self, director_id, first_name, last_name, email):
        return self.update_director_uc.execute(director_id, first_name, last_name, email)

    def delete_director(self, director_id):
        return self.delete_director_uc.execute(director_id)

    def get_director(self, director_id):
        return self.get_director_uc.execute(director_id)

    def get_all_directors(self):
        return self.get_all_directors_uc.execute()