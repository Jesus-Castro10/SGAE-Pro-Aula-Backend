from sgae_app.application.use_cases.student_uses_cases import *
from sgae_app.domain.entities.student import Student

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class StudentService:
    def __init__(self,
                 create_student_uc: CreateStudent,
                 update_student_uc: UpdateStudent,
                 delete_student_uc: DeleteStudent,
                 get_all_students_uc: GetAllStudents,
                 get_student_uc: GetStudent):
        
        self.create_student_uc = create_student_uc
        self.update_student_uc = update_student_uc
        self.delete_student_uc = delete_student_uc
        self.get_student_uc = get_student_uc
        self.get_all_students_uc = get_all_students_uc

    def create_student(self, student: Student):
        return self.create_student_uc.execute(student)

    def update_student(self, student_id, student: Student):
        return self.update_student_uc.execute(student_id, student)

    def delete_student(self, student_id):
        return self.delete_student_uc.execute(student_id)

    def get_student(self, student_id):
        return self.get_student_uc.execute(student_id)
    
    def get_all_students(self):
        return self.get_all_students_uc.execute()