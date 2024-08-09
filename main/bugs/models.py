import sys
sys.path.append("..")
from django.db import models
from customuser.models import Customuser
from projects.models import Projects

class Bug(models.Model):
    Project_Type = [
        ('feature', 'Feature'),
        ('bug', 'Bug')
    ]

    Feature_Choice = [
        ('new', 'New'),
        ('started', 'Started'),
        ('completed', 'Completed')
    ]

    Bug_Choice = [
        ('new', 'New'),
        ('started', 'Started'),
        ('resolved', 'Resolved')
    ]

    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    created_by = models.ForeignKey(Customuser, on_delete=models.CASCADE, related_name='created_by', limit_choices_to={'user_type__in': ['QA', 'MA']})
    assigned_to = models.ForeignKey(Customuser, on_delete=models.CASCADE, related_name='assigned_to', limit_choices_to={'user_type': 'DEV'})

    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)
    screenshot = models.ImageField(default='project_bug.jpeg', blank=True)
    type = models.CharField(max_length=7, choices=Project_Type)
    status = models.CharField(max_length=10, default='new')

    def __str__(self):
        return self.title
