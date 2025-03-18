from rest_framework import serializers
from .models import Photo
from apps.accounts.models import CustomUser

class PhotoSerializer(serializers.ModelSerializer):
    uploaded_by = serializers.PrimaryKeyRelatedField(read_only=True)  # Прибрали source, бо поле вже називається uploaded_by

    class Meta:
        model = Photo
        fields = ['id', 'title', 'image', 'uploaded_by', 'created_at']
        read_only_fields = ['uploaded_by', 'created_at']

    def create(self, validated_data):
        uploaded_by = self.context['request'].user
        return Photo.objects.create(uploaded_by=uploaded_by, **validated_data)  # Передаємо об’єкт