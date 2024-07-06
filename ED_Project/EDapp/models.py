from django.db import models

# Create your models here.
class userlogin(models.Model):
    UserName = models.CharField(max_length=10)
    PassWord = models.CharField(max_length = 10)
