from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from app_pets.serializers import ProfileSerializer, AnimalSerializer, AnimalDetailSerializer, ProfileDetailSerializer
from app_pets.models import Profile, Animal
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
from . import models

class ReadOnly(BasePermission):
  def has_permission(self, request, view):
    return request.method in SAFE_METHODS

class ProfileListView(ListCreateAPIView):
  queryset = models.Profile.objects.all()
  serializer_class = ProfileSerializer

class AnimalListView(ListCreateAPIView):
  queryset = Animal.objects.all()
  serializer_class = AnimalSerializer
  
# Used for Animal --> read-write-delete endpoints to represent a single model instance
class AnimalDetailView(RetrieveUpdateDestroyAPIView):
  queryset = Animal.objects.all()
  serializer_class = AnimalDetailSerializer

# Used for Profile --> read-write-delete endpoints to represent a single model instance
class ProfileDetailView(RetrieveUpdateDestroyAPIView):
  permission_classes = [IsAuthenticated, ]
  queryset = Profile.objects.all()
  serializer_class = ProfileDetailSerializer


#def get(self, request, format=None):
 #       content = {
  #          'status': 'request was permitted'
   #     }
    #    return Response(content)

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
  import pdb;pdb.set_trace()
  username = request.data.get("username")
  password = request.data.get("password")
  if username is None or password is None:
    return Response({'error': 'Please provide both username and password'},
      status=HTTP_400_BAD_REQUEST)
  user = authenticate(username=username, password=password)
  if not user:
    return Response({'error': 'Invalid Credentials'},
      status=HTTP_404_NOT_FOUND)
  token, _ = Token.objects.get_or_create(user=user)
  return Response({'token': token.key},
    status=HTTP_200_OK) 