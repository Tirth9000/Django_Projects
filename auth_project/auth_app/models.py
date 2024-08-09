from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserAuth(models.Model):
    email = models.EmailField(primary_key=True, max_length=255)
    name = models.CharField(max_length=100, default=None)
    password = models.CharField(max_length = 50)
    message = models.TextField()
     
    def __str__(self):
        return self.email
    
def set_password(raw_password):
    return make_password(raw_password)