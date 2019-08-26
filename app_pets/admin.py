from django.contrib import admin
from .models import Profile, Animal
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import ProfileCreationForm, ProfileChangeForm

admin.site.register(Animal)
class ProfileAdmin(UserAdmin):
    add_form = ProfileCreationForm
    form = ProfileChangeForm
    model = Profile
    list_display = ['email', 'username', 'name']

admin.site.register(Profile, ProfileAdmin)