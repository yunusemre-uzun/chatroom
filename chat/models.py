from django.db import models
from django.db.models import CASCADE
from django.contrib.auth.models import User
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.utils import timezone

max_number_of_friends = 100


class MyUser(User):
    username_validator = ASCIIUsernameValidator()
    friend_list = models.CharField(max_length=max_number_of_friends*151,default=":.")
    last_request = models.DateTimeField(default=timezone.now())
    def add_friend(self,username):
        if(self.isFriend(username)):
            return
        try:
            MyUser.objects.get(username=username)
        except:
            print("User does not exist")
            return
        if(not(self.friend_list[1:len(self.friend_list)-1].split(':'))[0]==''):
            print(self.friend_list[1:len(self.friend_list)-1].split(':'))
            self.friend_list = self.friend_list[0:len(self.friend_list)-1] + ":" + username + "."
            self.save()
            return
        self.friend_list = self.friend_list[1:len(self.friend_list)-1] + ":" + username + "."
        self.save()
    def remove_friend(self,username):
        if self.isFriend(username):
            list_of_friends=self.friend_list[0:len(self.friend_list)-1].split(':')
            list_of_friends.remove(username)
            new_friend_list = ":"
            for i in range(len(list_of_friends)):
                new_friend_list = new_friend_list + list_of_friends[i]
            self.friend_list = new_friend_list + "."
            self.save()
        else:
            print("User is not in your friend list")
            return
    def isFriend(self,username):
        list_of_friends=self.friend_list[0:len(self.friend_list)-1].split(':')
        if username in list_of_friends:
            return True
        else:
            return False


class Message(models.Model):
    def __str__(self):
        text = "<h4> <strong>"+str(self.sender)+"</strong> : "+str(self.text) +"(<i>" +str(self.date)+"</i>) </h4>"
        return text

    text = models.CharField(max_length=2048)
    sender = models.ForeignKey(MyUser,on_delete=models.CASCADE , related_name='sender')
    receiver = models.ForeignKey(MyUser , on_delete = models.CASCADE, related_name = 'receiver')
    is_read = models.BooleanField(default=False)
    date = models.DateTimeField('date wrote')
