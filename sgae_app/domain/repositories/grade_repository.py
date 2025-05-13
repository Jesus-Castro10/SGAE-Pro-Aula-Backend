from sgae_app.domain.entities.grade import Grade

class GradeRepository:
    def get_all(self):
        raise NotImplementedError

    def get_by_id(self, grade_id):
        raise NotImplementedError

    def save(self, grade: Grade):
        raise NotImplementedError

    def update(self, grade_id, grade: Grade):
        raise NotImplementedError

    def exists (self, grade: Grade):
        raise NotImplementedError
    
    def delete(self, grade_id):
        raise NotImplementedError