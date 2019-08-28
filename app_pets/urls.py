from django.urls import path, include
from app_pets.views import ProfileListView, ProfileDetailView, AnimalListView, AnimalDetailView, AnimalUpdateDetailView
from . import views
urlpatterns = [
    path('users/', ProfileListView.as_view(), name = 'api-users-list'),
    path('users/<int:pk>', ProfileDetailView.as_view(), name = 'api-users-detail'),
    path('animals/', AnimalListView.as_view(), name = 'api-animals-list'),
    path('animals/<int:pk>', AnimalDetailView.as_view(), name = 'api-animals-detail'),
    path('animals/<int:pk>/create-update', AnimalUpdateDetailView.as_view(), name = 'api-animals-update'),
]

    #path('login/', views.ProfileListView.as_view(), name = 'api-profile-auth'),
    