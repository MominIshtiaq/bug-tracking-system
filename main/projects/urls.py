from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('create/', views.createproject, name="createproject"),
    path('/search', views.search_view, name="search")
]
