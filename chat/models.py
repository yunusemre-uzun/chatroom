from django.db import models
from django.db.models import CASCADE
from django.contrib.auth.models import User
from django.contrib.auth.validators import ASCIIUsernameValidator

max_number_of_friends = 100

class MyUser(User):
    username_validator = ASCIIUsernameValidator()
    friend_list = models.CharField(max_length=max_number_of_friends*151,default=":.")
    def add_friend(self,username):
        if(self.isFriend(username)):
            return
        try:
            MyUser.objects.get(username=username)
        except:
            print("User does not exist")
            return
        self.friend_list = self.friend_list[0:len(self.friend_list)-1] + ":" + username + "."
        print("\n\n" + self.friend_list + "\n\n")
    def remove_friend(self,username):
        if self.isFriend(username):
            list_of_friends=self.friend_list[0:len(self.friend_list)-1].split(':')
            list_of_friends.remove(username)
            new_friend_list = ":"
            for i in range(len(list_of_friends)):
                new_friend_list = new_friend_list + list_of_friends[i]
            self.friend_list = new_friend_list + "."
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
        return self.text
    text = models.CharField(max_length=2048)
    sender = models.ForeignKey(MyUser,on_delete=models.CASCADE , related_name='sender')
    receiver = models.ForeignKey(MyUser , on_delete = models.CASCADE, related_name = 'receiver')
    is_read = models.BooleanField(default=0)
    date = models.DateTimeField('date wrote')


