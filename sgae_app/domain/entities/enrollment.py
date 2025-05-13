from typing import Optional, List
from dataclasses import field

class Enrollment:
    
    def __init__(self,id: int, student: Optional["Student"], group: Optional["Group"], academic_year: int, enrollment_date: str, status: str, observations: str):
        self.id = id
        self.student = student
        self.group = group
        self.academic_year = academic_year
        self.enrollment_date = enrollment_date
        self.status = status
        self.observations = observations

    def __repr__(self):
        return f"Enrollment(student_id={self.student}, course_id={self.group_id})"