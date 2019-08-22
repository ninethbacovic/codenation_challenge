from django.urls import path
from app_pets.views import UsersListView, AnimalsListView, AnimalsDetailView, UsersDetailView


urlpatterns = [
    path('users/', UsersListView.as_view(), name = 'api-users-list'),
    path('animals/', AnimalsListView.as_view(), name = 'api-animals-list'),
    path('animals/<int:pk>', AnimalsDetailView.as_view(), name = 'api-animals-detail'),
    path('users/<int:pk>', UsersDetailView.as_view(), name = 'api-users-detail'),
]


    