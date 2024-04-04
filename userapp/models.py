from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserLanguage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_language = models.CharField(max_length=50)
