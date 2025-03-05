from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Photo
from .serializers import PhotoSerializer

class PhotoUploadView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if request.user.role not in ['photographer', 'admin']:
            return Response({"error": "Тільки фотографи або адміністратори можуть завантажувати фото"}, status=403)
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(uploaded_by=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)