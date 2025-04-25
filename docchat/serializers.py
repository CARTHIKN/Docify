from rest_framework import serializers
from .models import User,Document
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if not user:
            raise serializers.ValidationError("Invalid credentials")
        return {'user': user}


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('profile', 'title', 'file')

    def validate_file(self, value):
        # You can add validation for the file type, size, etc., here
        if not value.name.endswith(('.pdf', '.docx', '.txt')):
            raise serializers.ValidationError("Invalid file type. Only PDF, DOCX, and TXT are allowed.")
        return value