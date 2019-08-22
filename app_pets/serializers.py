from rest_framework.serializers import ModelSerializer
from app_pets.models import Users, Animals
from rest_framework import serializers

class UsersSerializer(ModelSerializer):
  class Meta:
    model = Users
    id = serializers.IntegerField(read_only=True)
    fields = ('id', 'username', 'email', 'name', 'created', 'modified')
    

class UsersDetailSerializer(ModelSerializer):
  class Meta:
    model = Users
    id = serializers.IntegerField(read_only=True)
    fields = ('id','username', 'email', 'name', 'created', 'modified')


class AnimalsSerializer(ModelSerializer):
    class Meta:
        ordering = ['created']
        id = serializers.IntegerField(read_only=True)
        model = Animals
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

class AnimalsDetailSerializer(ModelSerializer):
    class Meta:
        model = Animals
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