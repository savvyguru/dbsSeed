from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import FileUploadParser
from .serializers import FileMetaSerializer
from quickstart.serializers import UserSerializer,TokenSerializer,FileMetaSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.settings import api_settings
from rest_framework import permissions
from rest_framework import generics
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework.parsers import FileUploadParser
from .models import File_Meta
from django.core import serializers
import re
from django.db import models
from .task import *


# Get the JWT settings, add these lines after the import/from lines
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

class RegisterUsers(generics.CreateAPIView):
    """
    POST auth/register/
    """
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        email = request.data.get("email", "")
        if not username and not password and not email:
            return Response(
                data={
                    "message": "username, password and email is required to register a user"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        new_user = User.objects.create_user(
            username=username, password=password, email=email
        )
        return Response(
            data=UserSerializer(new_user).data,
            status=status.HTTP_201_CREATED
        )

class LoginView(generics.CreateAPIView):
    """
    POST auth/login/
    """
    # This permission class will overide the global permission
    # class setting
    permission_classes = (permissions.AllowAny,)

    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # login saves the user’s ID in the session,
            # using Django’s session framework.
            login(request, user)
            serializer = TokenSerializer(data={
                # using drf jwt utility functions to generate a token
                "token": jwt_encode_handler(
                    jwt_payload_handler(user)
                )})
            serializer.is_valid()
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


# class UploadFile(APIView):
#     #check if file is .txt
#     def validate_file_extension(value):
#         if not value.name.endswith('.txt'):
#             raise ValidationError(u'Error message')

#     #token authentication
#     permission_classes = (permissions.IsAuthenticated,)
#     parser_class = (FileUploadParser,)

#     def post(self, request, *args, **kwargs):

#       file_serializer = FileMetaSerializer(data=request.data)

#       if file_serializer.is_valid():
#           file_serializer.save()
#           return Response(file_serializer.data, status=status.HTTP_201_CREATED)
#       else:
#           return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FileUploadView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

      file_serializer = FileMetaSerializer(data=request.data)

      if file_serializer.is_valid():
          file_serializer.save()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListFile(APIView):
    #list all the files in the database
    permission_classes = (permissions.IsAuthenticated,)
    #permission_classes = (permissions.AllowAny,)
    def get(self,request):
        files_list = []
        querysets = File_Meta.objects.all()
        for queryset in querysets:
            file_dict = {}
            file_dict["pk"] = queryset.pk
            file_dict["file_name"] = queryset.file.name
            file_dict["file_size"] = queryset.file.size
            file_dict["file_path"] = queryset.file.path
            file_dict["score"] = str(queryset.score)
            file_dict["timestamp"] = str(queryset.timestamp)
            files_list.append(file_dict)

        #data = serializers.serialize('json', queryset)
        return Response(files_list, status=status.HTTP_201_CREATED)

# class ListFile(APIView):
#     #list all the files in the database
#     permission_classes = (permissions.IsAuthenticated,)
#     def get(self,request):
#         queryset = File_Meta.objects.all()
#         serializer_class = FileMetaSerializer
#         data = serializers.serialize('json', queryset)
#         return Response(data, status=status.HTTP_201_CREATED)
        #token authentication
        
class updateScore(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self,request):
        permission_classes = (permissions.AllowAny,)
        updateScoreTask.delay()
        return Response("Update Complete", status=status.HTTP_201_CREATED)

