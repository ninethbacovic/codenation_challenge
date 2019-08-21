from django.urls import path
from app_pets.views import UsersListView, AnimalsListView


urlpatterns = [
    path('users/', UsersListView.as_view(), name = 'api-users-list'),
    path('animals/', AnimalsListView.as_view(), name = 'api-animals-list')
]


    