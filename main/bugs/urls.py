from django.urls import path
from . import views

app_name = 'bugs'

urlpatterns = [
    path('<int:project_id>', views.bugs, name="bugs"),
    path('create/<int:project_id>/<str:type>', views.create, name="create"),
    path('change_status/<int:bug_id>/<int:project_id>/<str:status>', views.change_status, name="change_status"),
    path('delete/<int:project_id>/<int:bug_id>', views.delete, name="delete")
]
