from rest_framework import serializers
from .models import Photo

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'title', 'image', 'uploaded_by', 'created_at']
        read_only_fields = ['uploaded_by', 'created_at']