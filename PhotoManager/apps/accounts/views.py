# apps/accounts/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterAdminSerializer

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