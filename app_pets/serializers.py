from rest_framework.serializers import ModelSerializer
from app_pets.models import Profile, Animal
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):
  class Meta:
    model = User
    fields = ('username', 'email', 'first_name', 'password')

class ProfileSerializer(ModelSerializer):
  user = UserSerializer()
  class Meta:
    model = Profile
    fields = ('id', 'user', 'created', 'modified')
    

class ProfileDetailSerializer(ModelSerializer):
  class Meta:
    model = Profile
    fields = ('id','username', 'email', 'name', 'created', 'modified')

class AnimalSerializer(ModelSerializer):
  class Meta:
    ordering = ['created']
    model = Animal
    fields = [
    'contact',
      'id',
      'name',
      'description',
      'image',
      'age',
      'color',
      'gender',
      'specie',
      'size',
      'category',
      'location',
      'city',
      'state',
      'created',
      'modified',
    ]

class AnimalDetailSerializer(ModelSerializer):
  class Meta:
    model = Animal
    id = serializers.IntegerField(read_only=True)
    fields = ['contact',
      'id',
      'name',
    'description',
      'image',
      'age',
      'color',
      'gender',
      'specie',
      'size',
      'category',
      'location',
      'city',
      'state',
      'created',
      'modified',
      ]