from django.urls import path
from app_pets.views import ProfileListView, AnimalListView, AnimalDetailView, ProfileDetailView, login

urlpatterns = [
    path('users/', ProfileListView.as_view(), name = 'api-users-list'),
    path('animals/', AnimalListView.as_view(), name = 'api-animals-list'),
    path('animals/<int:pk>', AnimalDetailView.as_view(), name = 'api-animals-detail'),
    path('users/<int:pk>', ProfileDetailView.as_view(), name = 'api-users-detail'),
    path('login', login)
]


    