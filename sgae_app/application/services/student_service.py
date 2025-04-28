from sgae_app.domain.use_cases.student import CreateStudent, UpdateStudent, DeleteStudent, GetStudent
from sgae_app.infrastructure.repositories.djstudent_repository import StudentRepository

class StudentService:
    def __init__(self,
                 repository: StudentRepository,
                 create_student: CreateStudent,
                 update_student: UpdateStudent,
                 delete_student: DeleteStudent,
                 get_student: GetStudent):
        self.repository = repository
        self.create_student = create_student
        self.update_student = update_student
        self.delete_student = delete_student
        self.get_student = get_student

    def create_student(self, first_name, last_name, email):
        return self.create_student.execute(first_name, last_name, email)

    def update_student(self, student_id, first_name, last_name, email):
        return self.update_student.execute(student_id, first_name, last_name, email)

    def delete_student(self, student_id):
        return self.delete_student.execute(student_id)

    def get_student(self, student_id):
        return self.get_student.execute(student_id)