# views.py
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .exceptions import AuthenticationFailed
from .serializers import *
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken

class PasswordChangeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = PasswordChangeSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            old_password = serializer.validated_data["old_password"]
            new_password = serializer.validated_data["new_password"]

            if not user.check_password(old_password):
                raise AuthenticationFailed(message="La contraseña antigua es incorrecta.")

            user.set_password(new_password)
            user.save()

            return Response(
                {"message": "Contraseña actualizada exitosamente."},
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class LoginView(TokenObtainPairView):
#     permission_classes = [permissions.AllowAny]

#     serializer_class = TokenObtainSerializer
    
class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = TokenObtainSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        data = serializer.data
        
        username=data["username"]
        password=data["password"]
         
        if not User.objects.filter(username=username).exists():
            raise AuthenticationFailed(message="Usuario o contraseña incorrecta.")
        
        user = User.objects.get(username=username)
        if not user.check_password(password):
            raise AuthenticationFailed(message="Usuario o contraseña incorrecta.")
        
        if not user.is_active:
            raise AuthenticationFailed(message="El usuario no está activo.")
        
        token = RefreshToken.for_user(user)
        access = token.access_token
        access['user_type'] = user.user_type
        access['username'] = user.username
        return Response({"access":str(access), "refresh":str(token)}, status=status.HTTP_200_OK)