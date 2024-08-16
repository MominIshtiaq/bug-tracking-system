from django.urls import path, include
from . import views

app_name = "customuser"

urlpatterns = [
    path('', views.index, name="index"),
    path('signup/', views.signup_redirect, name="signup_redirect"),
    path('signup/<str:actor>', views.signup, name='signup'),
    path('login', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
]
