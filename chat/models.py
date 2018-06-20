from django.db import models

class Message(models.Model):
    def __str__(self):
        return self.text
    text = models.CharField(max_length=2048)
    sender = models.CharField(max_length=1024,default="user")
    receiver = models.CharField(max_length=1024,default="user")
    is_read = models.BooleanField(default=0)
    date = models.DateTimeField('date wrote')

class User(models.Model):
    def __str__(self):
        return self.getnickname()
    nickname = models.CharField(max_length=1024)
