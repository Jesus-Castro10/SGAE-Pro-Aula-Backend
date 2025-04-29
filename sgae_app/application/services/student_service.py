from sgae_app.domain.use_cases.student import CreateStudent, UpdateStudent, DeleteStudent, GetStudent
from sgae_app.domain.entities.student import Student

class StudentService:
    def __init__(self,
                 create_student_uc: CreateStudent,
                 update_student_uc: UpdateStudent,
                 delete_student_uc: DeleteStudent,
                 get_student_uc: GetStudent):
        self.create_student_uc = create_student_uc
        self.update_student_uc = update_student_uc
        self.delete_student_uc = delete_student_uc
        self.get_student_uc = get_student_uc

    def create_student(self, student: Student):
        return self.create_student_uc.execute(
            student
        )

    def update_student(self, student_id, first_name, last_name, email):
        return self.update_student_uc.execute(student_id, first_name, last_name, email)

    def delete_student(self, student_id):
        return self.delete_student_uc.execute(student_id)

    def get_student(self, student_id):
        return self.get_student_uc.execute(student_id)