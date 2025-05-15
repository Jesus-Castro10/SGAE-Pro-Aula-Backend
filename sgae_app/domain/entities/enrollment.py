from datetime import date

class Enrollment:
    VALID_STATUSES = {'active', 'withdrawn', 'graduated'}

    def __init__(self, id: int = None, student=None, group=None, academic_year: int = None, enrollment_date: date = None, status: str = 'active', observations: str = None):
        if academic_year < 2000:
            raise ValueError("El año académico debe ser razonable.")
        if status not in self.VALID_STATUSES:
            raise ValueError(f"Estado inválido: {status}")

        self.id = id
        self.student = student
        self.group = group
        self.academic_year = academic_year
        self.enrollment_date = enrollment_date or date.today()
        self.status = status
        self.observations = observations

    def is_active(self):
        return self.status == 'active'
