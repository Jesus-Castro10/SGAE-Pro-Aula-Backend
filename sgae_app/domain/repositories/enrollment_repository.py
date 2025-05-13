from sgae_app.domain.entities.enrollment import Enrollment

class EnrollmentRepository:
    def get_all(self):
        raise NotImplementedError

    def get_by_id(self, id):
        raise NotImplementedError

    def save(self, enrollment: Enrollment):
        raise NotImplementedError

    def update(self, id, Enrollment: Enrollment):
        raise NotImplementedError

    def exists (self, enrollment: Enrollment):
        raise NotImplementedError
    
    def delete(self, id):
        raise NotImplementedError