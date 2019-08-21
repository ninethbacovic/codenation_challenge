from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from app_pets.serializers import UsersSerializer, AnimalsSerializer
from app_pets.models import Users, Animals

class UsersListView(ListCreateAPIView):
  queryset = Users.objects.all()
  serializer_class = UsersSerializer

class AnimalsListView(ListCreateAPIView):
  queryset = Animals.objects.all()
  serializer_class = AnimalsSerializer