from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
  HTTP_400_BAD_REQUEST,
  HTTP_404_NOT_FOUND,
  HTTP_200_OK
)
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework.response import Response
from rest_framework import permissions

from app_pets.serializers import (
  ProfileSerializer, 
  ProfileDetailSerializer, 
  AnimalSerializer, 
  AnimalDetailSerializer, 
  AnimalUpdateDetailSerializer, 
  AnimalNewDetailSerializer
)
from app_pets.models import Profile, Animal
from . import models

# Profile List --> read-only endpoints of all profiles. Everyone can see it.
class ProfileListView(ListAPIView): 
  permission_classes = [permissions.AllowAny]
  queryset = models.Profile.objects.all()
  serializer_class = ProfileSerializer

# Profile detail -->just for who has login to read-write-delete endpoints to represent a single model instance.
class ProfileDetailView(RetrieveUpdateDestroyAPIView):
  permission_classes = [permissions.IsAuthenticated]
  queryset = Profile.objects.all()
  serializer_class = ProfileDetailSerializer

# Animal list --> used for read-only endpoints. Everyone can see it.
class AnimalListView(ListAPIView):
  permission_classes = [permissions.AllowAny]
  queryset = Animal.objects.all()
  serializer_class = AnimalSerializer

# Animal detail --> used for read-only endpoints. Everyone can see it.
class AnimalDetailView(RetrieveAPIView):
  permission_classes = [permissions.AllowAny]
  queryset = Animal.objects.all()
  serializer_class = AnimalDetailSerializer

# Animal Update Detail - just for who has login to read-write-delete endpoints to represent a single model instance
class AnimalUpdateDetailView(RetrieveUpdateDestroyAPIView):
  permission_classes = [permissions.IsAuthenticated]
  queryset = Animal.objects.all()
  serializer_class = AnimalUpdateDetailSerializer

# Create a new animal - just for who has login to create endpoints to represent a single model instance
class AnimalNewDetailView(CreateAPIView):
  permission_classes = [permissions.IsAuthenticated]
  queryset = Animal.objects.all()
  serializer_class = AnimalNewDetailSerializer

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
  username = request.data.get("username")
  password = request.data.get("password")
  if username is None or password is None:
    return Response({'error': 'Please provide both username and password'},
      status=HTTP_400_BAD_REQUEST)

  user = authenticate(username=username, password=password)
  if not user:
    return Response({'error': 'Invalid Credentials'}, status=HTTP_404_NOT_FOUND)

  token, _ = Token.objects.get_or_create(user=user)
  return Response({'token': token.key}, status=HTTP_200_OK) 
