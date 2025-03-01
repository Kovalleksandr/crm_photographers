# apps/accounts/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import RegisterAdminSerializer, InviteSerializer, RegisterWithInviteSerializer
from .models import CustomUser

class RegisterAdminView(APIView):
    def post(self, request):
        serializer = RegisterAdminSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "message": "Адміністратор створений",
                "user_id": user.id,
                "organization": user.organization.name
            })
        return Response(serializer.errors, status=400)

class InviteUserView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        if request.user.role != 'admin':
            return Response({"error": "Тільки адміністратор може створювати запрошення"}, status=403)
        serializer = InviteSerializer(data=request.data)
        if serializer.is_valid():
            invitation = serializer.save(organization=request.user.organization)
            invite_link = f"http://127.0.0.1:8000/api/accounts/register-with-invite/?code={invitation.code}"
            return Response({"invite_link": invite_link})
        return Response(serializer.errors, status=400)

class RegisterWithInviteView(APIView):
    def post(self, request):
        serializer = RegisterWithInviteSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "message": f"Користувач із роллю {user.role} створений",
                "user_id": user.id
            })
        return Response(serializer.errors, status=400)