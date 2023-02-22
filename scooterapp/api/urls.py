from api import views
from django.urls import path


urlpatterns = [
    path('v1/userlist/', views.UserViewList.as_view()),
    path('v1/scooterlist', views.ScooterViewList.as_view()),
    path('v1/triplist', views.TripViewList.as_view()),
    path('v1/scooterdetail/<int:pk>/', views.ScooterApi.as_view()),
]