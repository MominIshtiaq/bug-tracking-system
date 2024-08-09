from django.db import models
from django.contrib.auth.models import AbstractUser

# User Model
class User(AbstractUser):
    class Role(models.TextChoices):
        MANAGER = "MA", "Manager"
        DEVELOPER = "DEV", "Developer"
        QUALITY_ASSURANCE = "QA", "Quality Assurance"

    email = models.EmailField(max_length=255, unique=True)
