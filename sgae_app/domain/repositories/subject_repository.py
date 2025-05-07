from sgae_app.domain.entities.subject import Subject

class SubjectRepository:
    def get_all(self):
        raise NotImplementedError

    def get_by_id(self, subject_id):
        raise NotImplementedError

    def save(self, subject: Subject):
        raise NotImplementedError

    def update(self, subject_id, subject: Subject):
        raise NotImplementedError

    def exists (self, subject: Subject):
        raise NotImplementedError
    
    def delete_subject(self, subject_id):
        raise NotImplementedError