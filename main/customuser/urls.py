from django.urls import path, include
from . import views

app_name = "customuser"

urlpatterns = [
    path('', views.index, name="index"),
    path('signin/<str:actor>', views.signin, name='signin'),
    path('login', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
]
