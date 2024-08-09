from django.contrib.auth.models import AbstractUser
from django.db import models

# User Model
class Customuser(AbstractUser):
    Role = [
        ('DEV', 'Developer'),
        ('QA', 'Quality Assurance'),
        ('MA', 'Manager'),
    ]

    email = models.EmailField()
    user_type = models.CharField(max_length=3, choices=Role)
    image = models.ImageField(default="default_user_img.jpg", blank= True)

    def __str__(self):
        return self.username