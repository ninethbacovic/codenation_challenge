from rest_framework.serializers import ModelSerializer
from app_pets.models import Profile, Animal
from rest_framework import serializers
from . import models

class ProfileSerializer(ModelSerializer):
  class Meta:
    model = models.Profile
    id = serializers.IntegerField(read_only=True)
    fields = ('id', 'username', 'email', 'name', 'created', 'modified')
    #fields = ('id', 'username', 'password', 'email', 'name', 'created', 'modified')
    

class ProfileDetailSerializer(ModelSerializer):
  class Meta:
    model = Profile
    id = serializers.IntegerField(read_only=True)
    fields = ('id','username', 'email', 'name','created', 'modified')


class AnimalSerializer(ModelSerializer):
    class Meta:
        ordering = ['created']
        id = serializers.IntegerField(read_only=True)
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