class SubjectAssignment:
    def __init__(self, id: int = None, teacher=None, subject=None, group=None, academic_year: int = None, classroom=None):
        if academic_year < 2000:
            raise ValueError("Año académico inválido.")

        self.id = id
        self.teacher = teacher
        self.subject = subject
        self.group = group
        self.academic_year = academic_year
        self.classroom = classroom
