from sgae_app.application.use_cases.teacher_uses_cases import *
from sgae_app.domain.entities.teacher import Teacher


class TeacherService:
    def __init__(self,
                 create_teacher_uc: CreateTeacher,
                 update_teacher_uc: UpdateTeacher,
                 delete_teacher_uc: DeleteTeacher,
                 get_all_teachers_uc: GetAllTeachers,
                 get_teacher_uc: GetTeacher):
        
        self.create_teacher_uc = create_teacher_uc
        self.update_teacher_uc = update_teacher_uc
        self.delete_teacher_uc = delete_teacher_uc
        self.get_teacher_uc = get_teacher_uc
        self.get_all_teachers_uc = get_all_teachers_uc

    def create_teacher(self, teacher: Teacher):
        return self.create_teacher_uc.execute(teacher)

    def update_teacher(self, teacher_id, Teacher: Teacher):
        return self.update_teacher_uc.execute(teacher_id, Teacher)

    def delete_teacher(self, teacher_id):
        return self.delete_teacher_uc.execute(teacher_id)

    def get_teacher(self, teacher_id):
        return self.get_teacher_uc.execute(teacher_id)
    
    def get_all_teachers(self):
        return self.get_all_teachers_uc.execute()