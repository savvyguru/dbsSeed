from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from .models import File_Meta
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(min_length=8,write_only=True)

    class Meta:
        model = User
        fields = ('id','username', 'email', 'password')

    def create(self, validated_data):
        #hash password using make_password()
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
             make_password(validated_data['password']))
        user.save()
        return user

class TokenSerializer(serializers.Serializer):
    """
    This serializer serializes the token data
    """
    token = serializers.CharField(max_length=255)

class FileMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = File_Meta
        #fields = ("score")
        fields = ("__all__")
