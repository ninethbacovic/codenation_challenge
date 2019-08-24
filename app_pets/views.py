from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from app_pets.serializers import UsersSerializer, AnimalsSerializer, AnimalsDetailSerializer, UsersDetailSerializer
from app_pets.models import Users, Animals

class UsersListView(ListCreateAPIView):
  queryset = Users.objects.all()
  serializer_class = UsersSerializer

class AnimalsListView(ListCreateAPIView):
  queryset = Animals.objects.all()
  serializer_class = AnimalsSerializer

# Used for Animals --> read-write-delete endpoints to represent a single model instance
class AnimalsDetailView(RetrieveUpdateDestroyAPIView):
  queryset = Animals.objects.all()
  serializer_class = AnimalsDetailSerializer

# Used for Users --> read-write-delete endpoints to represent a single model instance
class UsersDetailView(RetrieveUpdateDestroyAPIView):
  queryset = Users.objects.all()
  serializer_class = UsersDetailSerializer