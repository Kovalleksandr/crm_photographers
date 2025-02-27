# apps/accounts/serializers.py
from rest_framework import serializers
from .models import CustomUser, Invitation

class RegisterAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email'],
            role='admin'
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class InviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitation
        fields = ['role']

class RegisterWithInviteSerializer(serializers.ModelSerializer):
    invite_code = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'invite_code']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        invite_code = validated_data.pop('invite_code')
        invitation = Invitation.objects.filter(code=invite_code, is_used=False).first()
        if not invitation:
            raise serializers.ValidationError("Недійсний або використаний код запрошення")
        
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email'],
            role=invitation.role,
            organization=invitation.organization
        )
        user.set_password(validated_data['password'])
        user.save()
        invitation.is_used = True
        invitation.save()
        return user