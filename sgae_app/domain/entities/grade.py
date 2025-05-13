from typing import List, Optional

class Grade:
    
    student: Optional["Student"] = None
    subject: Optional["Subject"] = None
    teacher: Optional["Teacher"] = None
    
    def __init__(self, id: int, value: float, period: str, student: Optional["Student"], subject: Optional["Subject"], teacher: Optional["Teacher"]):
        self.id = id
        self.value = value
        self.period = period
        self.student = student
        self.subject = subject
        self.teacher = teacher

    def __repr__(self):
        return f"Grade(id={self.id}, value='{self.value}')"