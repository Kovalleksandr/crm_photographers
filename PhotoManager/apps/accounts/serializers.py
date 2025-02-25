from rest_framework import serializers
from django.contrib.auth import get_user_model
from apps.multi_tenancy.models import Organization

User = get_user_model()

class RegisterAdminSerializer(serializers.ModelSerializer):
    organization_name = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'organization_name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        org_name = validated_data.pop('organization_name')
        user = User.objects.create_user(**validated_data, role='admin')
        
        # Створюємо організацію та базу даних
        organization = Organization.objects.create(name=org_name, owner=user)
        
        return user
