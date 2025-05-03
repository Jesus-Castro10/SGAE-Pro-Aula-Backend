from sgae_app.domain.exceptions.exceptions import DomainException

class StudentAlreadyExistsException(DomainException):
    pass

class StudentNotFoundException(DomainException):
    pass