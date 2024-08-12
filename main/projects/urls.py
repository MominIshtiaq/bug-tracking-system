from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('logout/', views.logout, name="logout"),
    path('create/', views.createproject, name="createproject")
]
