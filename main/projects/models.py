import sys
sys.path.append("..")
from django.db import models
from customuser.models import Customuser
from django.urls import reverse

class Projects(models.Model):
    manager = models.ForeignKey(Customuser, on_delete=models.CASCADE,limit_choices_to={'user_type': 'MA'})
    name = models.CharField(max_length=200)
    detail = models.TextField()
    image = models.ImageField(default="project_img_bg_not.png", blank= True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("project_detail", args=[str(self.id)])
    
    