from django.db import models
from django.db.models import CASCADE
from django.contrib.auth.models import User
from django.contrib.auth.validators import ASCIIUsernameValidator

class MyUser(User):
    username_validator = ASCIIUsernameValidator()

class Message(models.Model):
    def __str__(self):
        return self.text
    text = models.CharField(max_length=2048)
    sender = models.CharField(max_length=1024,default="user")
    receiver = models.CharField(max_length=1024,default="user")
    is_read = models.BooleanField(default=0)
    date = models.DateTimeField('date wrote')


