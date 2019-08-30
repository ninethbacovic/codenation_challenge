from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms

class Profile(AbstractUser):
  name = models.CharField(blank=False, max_length=255)
  created = models.DateTimeField(auto_now=True)
  modified = models.DateTimeField(auto_now_add=True)
  image = models.ImageField(upload_to='imgs/profile/', blank=True)

  def __str__(self):
    return self.email

class Animal(models.Model):

  contact = models.ForeignKey(Profile, on_delete = models.CASCADE)
  name = models.CharField(max_length = 255,null = False,blank = False)
  description = models.TextField(blank = True)
  image = models.ImageField(upload_to='imgs/animals/', blank=True)
  age = models.IntegerField(default = 0,null = False,blank = False)
  color = models.CharField(max_length = 255,null = False,blank = False)
  FEMEA = 'F'
  MACHO = 'M'
  GENDER_CHOICES = ((FEMEA, 'femea'),(MACHO, 'macho'),)
  gender = models.CharField(default = FEMEA,max_length = 1,choices = GENDER_CHOICES)
  CACHORRO = 'cachorro'
  GATO = 'gato'
  SPECIE_CHOICES = ((CACHORRO, 'cachorro'),(GATO, 'gato'),)
  specie = models.CharField(default = CACHORRO,max_length = 225,choices = SPECIE_CHOICES)
  PEQUENO = 'pequeno'
  MEDIO = 'medio'
  GRANDE = 'grande'
  EXTRA = 'extra grande'
  SIZE_CHOICES = ((PEQUENO, 'pequeno'),(MEDIO, 'medio'),(GRANDE, 'grande'),(EXTRA, 'extra grande'))
  size = models.CharField(default = PEQUENO,max_length = 225,choices = SIZE_CHOICES)
  ACHADO = 'achado'
  PERDIDO = 'perdido'
  ADOCAO = 'adoção' 
  CATEGORY_CHOICES = ((ACHADO, 'achado'),(PERDIDO, 'perdido'),(ADOCAO, 'adoção'),)
  category = models.CharField(default = ACHADO,max_length = 225,choices = CATEGORY_CHOICES)
  location = models.CharField(max_length = 255,)
  city = models.CharField(max_length = 255,)
  state = models.CharField(max_length = 255,)
  created = models.DateTimeField(auto_now=True)
  modified = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ['created']

  def __str__(self):
    return self.name
