from rest_framework import serializers
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Account


class AccountSerializer(serializers.Serializer):
    email = serializers.EmailField(allow_null=False)
    password = serializers.CharField(allow_null=False)
    full_name = serializers.CharField(max_length=64, required=False)
    is_active = serializers.BooleanField(default=True, required=False)
    date_joined = serializers.DateField(required=False)
    is_deleted = serializers.BooleanField(default=False)
    birth_date = serializers.DateField(required=False)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.is_deleted = validated_data.get('is_deleted', instance.is_deleted)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.save()
        return instance

    def create(self, validated_data):
        return Account.objects.create_user(**validated_data)


class AccountTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['user_id'] = user.id
        return token
