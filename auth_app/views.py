# views.py
from django.http import JsonResponse
from rest_framework import status, permissions
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from .serializers import PasswordChangeSerializer
from .models import User

class PasswordChangeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = PasswordChangeSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            old_password = serializer.validated_data["old_password"]
            new_password = serializer.validated_data["new_password"]

            if not user.check_password(old_password):
                raise AuthenticationFailed("La contraseña antigua es incorrecta.")

            user.set_password(new_password)
            user.save()

            return Response(
                {"message": "Contraseña actualizada exitosamente."},
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateUserTest(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        try:
            user, created = User.objects.get_or_create(
                username='jesusadmin1',
                defaults={
                    'password': 'jesusadmin123',
                    'role': 'admin',
                    'enabled': True
                }
            )

            if not created:
                return Response({'message': '⚠️ El usuario ya existe.'}, status=status.HTTP_400_BAD_REQUEST)

            user.set_password('jesusadmin123')
            user.save()

            return Response({'message': '✅ Usuario creado correctamente.'}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
