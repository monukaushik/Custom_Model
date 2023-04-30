import email
from operator import mod
from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import *


class userdetail(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)


class User(AbstractUser):
    username=None
    email=models.EmailField(unique=True)
    mobile=models.IntegerField(default=False,null=True, blank=True)
    
    object=UserManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS = [] 
    
    