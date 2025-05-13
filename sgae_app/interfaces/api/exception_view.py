from rest_framework.response import Response
from rest_framework.views import exception_handler
from rest_framework import status
from sgae_app.domain.exceptions.exceptions import DomainException
import logging
from auth_app.exceptions import AuthException

logger = logging.getLogger(__name__)

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        return response
    
    if isinstance(exc, DomainException):
        return Response({
            'message': exc.message,
            'errors': exc.errors if exc.errors else None,
        }, status=exc.status_code)
    
    if isinstance(exc, AuthException):
        return Response({
            'message': exc.message,
            'errors': exc.errors if exc.errors else None,
        }, status=exc.status_code)
        
    logger.error("Unhandled exception", exc_info=exc)

    return Response({
        'error': 'Error interno del servidor.',
        'detail': str(exc),
    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
