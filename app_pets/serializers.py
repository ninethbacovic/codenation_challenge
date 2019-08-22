from rest_framework.serializers import ModelSerializer
from app_pets.models import Users, Animals

class UsersSerializer(ModelSerializer):
  class Meta:
    model = Users
    fields = ('username', 'email', 'name', 'created', 'modified')

class UsersDetailSerializer(ModelSerializer):
  class Meta:
    model = Users
    fields = ('username', 'email', 'name', 'created', 'modified')


class AnimalsSerializer(ModelSerializer):
    class Meta:
        model = Animals
        fields = ['contact',
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
          ]

class AnimalsDetailSerializer(ModelSerializer):
    class Meta:
        model = Animals
        fields = ['contact',
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
          ]