from sgae_app.application.use_cases.classroom_uses_cases import *
from sgae_app.domain.entities.classroom import ClassRoom

class ClassRoomService:
    def __init__(self,
                 create_classroom_uc: CreateClassroom,
                 update_classroom_uc: UpdateClassroom,
                 delete_classroom_uc: DeleteClassroom,
                 get_classroom_uc: GetClassroom,
                 get_all_classrooms_uc: GetAllClassrooms):

        self.create_classroom_uc = create_classroom_uc
        self.update_classroom_uc = update_classroom_uc
        self.delete_classroom_uc = delete_classroom_uc
        self.get_classroom_uc = get_classroom_uc
        self.get_all_classrooms_uc = get_all_classrooms_uc

    def create(self, classroom: ClassRoom):
        return self.create_classroom_uc.execute(classroom)

    def update(self, classroom_id, classroom: ClassRoom):
        return self.update_classroom_uc.execute(classroom_id, classroom)

    def delete(self, classroom_id):
        return self.delete_classroom_uc.execute(classroom_id)

    def get(self, classroom_id):
        return self.get_classroom_uc.execute(classroom_id)

    def get_all(self):
        return self.get_all_classrooms_uc.execute()
