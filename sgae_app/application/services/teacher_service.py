from sgae_app.application.use_cases.teacher_uses_cases import *
from sgae_app.domain.entities.teacher import Teacher
<<<<<<< HEAD
from sgae_app.application.services.user_creator_service import UserCreatorService
=======

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
>>>>>>> 731176f3be5f8aaa08d03f64535589ca80e5bd1f

class TeacherService:
    def __init__(self,
                 create_teacher_uc: CreateTeacher,
                 update_teacher_uc: UpdateTeacher,
                 delete_teacher_uc: DeleteTeacher,
                 get_all_teachers_uc: GetAllTeachers,
<<<<<<< HEAD
                 get_teacher_uc: GetTeacher,
                 user_creator: UserCreatorService):
=======
                 get_teacher_uc: GetTeacher):
>>>>>>> 731176f3be5f8aaa08d03f64535589ca80e5bd1f
        
        self.create_teacher_uc = create_teacher_uc
        self.update_teacher_uc = update_teacher_uc
        self.delete_teacher_uc = delete_teacher_uc
        self.get_teacher_uc = get_teacher_uc
        self.get_all_teachers_uc = get_all_teachers_uc
<<<<<<< HEAD
        self.user_creator = user_creator

    def create_teacher(self, teacher: Teacher):
        teacher.user = self.user_creator.create_user(teacher.email, teacher.id_card, 'teacher')
=======

    def create_teacher(self, teacher: Teacher):
>>>>>>> 731176f3be5f8aaa08d03f64535589ca80e5bd1f
        return self.create_teacher_uc.execute(teacher)

    def update_teacher(self, teacher_id, teacher: Teacher):
        return self.update_teacher_uc.execute(teacher_id, teacher)

    def delete_teacher(self, teacher_id):
        return self.delete_teacher_uc.execute(teacher_id)

    def get_teacher(self, teacher_id):
        return self.get_teacher_uc.execute(teacher_id)
    
    def get_all_teachers(self):
        return self.get_all_teachers_uc.execute()