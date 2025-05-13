class AuthException(Exception):
    def __init__(self, message="Error en el modulo de seguridad", status_code=401, errors=None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.errors = errors
        
class AuthenticationFailed(AuthException):
    def __init__(self, message="Credenciales inválidas", status_code=401, errors=None):
        super().__init__(message, status_code, errors)
        
class TokenExpiredException(AuthException):
    def __init__(self, message="Token expirado", status_code=401, errors=None):
        super().__init__(message, status_code, errors)
        
class TokenInvalidException(AuthException):
    def __init__(self, message="Token inválido", status_code=401, errors=None):
        super().__init__(message, status_code, errors)
        
class TokenNotFoundException(AuthException):
    def __init__(self, message="Token no encontrado", status_code=401, errors=None):
        super().__init__(message, status_code, errors)