from django.db import models

# User Model
class Customuser(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField()
    user_type = models.CharField(max_length=20)
    image = models.ImageField(default="default_user_img.jpg", blank= True)

    def __str__(self):
        return self.username