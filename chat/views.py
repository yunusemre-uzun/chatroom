import json

from  django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.shortcuts import render
import datetime
import time

from django.http import HttpResponse, HttpResponseRedirect, request
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.views import View
from .models import Message, MyUser
from .forms import *


class IndexView(View):
    def get(self,request):
        form = UserForm()
        return render(request,'chat/index.html',{'form':form})
    def post(self,request):
        form = UserForm()
        return render(request,'chat/index.html',{'form':form})

class ChatView(View):
    def get(self,request, **kwargs):

        username = kwargs['username']
        receiverName = kwargs['receiver']
        user = MyUser.objects.get(username= username)
        receiver = MyUser.objects.get(username = receiverName)
        message_list = Message.objects.filter(Q(sender = user.id,receiver = receiver.id) | Q(sender = receiver.id, receiver = user.id)).order_by('-date')[:10:-1]
        form = MessageForm()
        context = {'roomName':'','messageList':message_list,'form':form, 'username':username ,'receiver':receiver}
        if (request.is_ajax()):
            context = {'messageList': message_list,'roomName':'2' }
            return render(request, 'chat/ajaxChatroom.html', context)

        return render(request,'chat/chatroom.html',context)

    def post(self, request, **kwargs):
        username = kwargs['username']
        receiver = kwargs['receiver']
        form = MessageForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            print('Hello')
            user = MyUser.objects.get(username=username)
            receiver = MyUser.objects.get(username = receiver)
            new_message = form.cleaned_data['new_message']
            message_object = Message(text=new_message,sender= user,receiver = receiver ,date=timezone.now())
            message_object.save()
        return self.get(request, username = username , receiver = receiver)


class UsernameView(View):
    def post(self,request):
        form = UserForm(request.POST)
        if form.is_valid():
            username = str(form.cleaned_data['username'])
            password = str(form.cleaned_data['password'])
            try:
                MyUser.objects.get(username=username)
            except:
                MyUser.DoesNotExist()
            u = MyUser.objects.get(username=username)
            if(u.check_password(password)):
                u.is_active=True
                return HttpResponseRedirect(username+'/friends/')
            else:
                return HttpResponseRedirect('/')
class SignUpView(View):
    def get(self,request):
        form = SignUpForm()
        return render(request,'chat/signup.html',{'form':form})

    def post(self,request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            new_user = MyUser()
            new_user.username = str(form.cleaned_data['username'])
            new_user.set_password(str(form.cleaned_data['password']))
            new_user.first_name = str(form.cleaned_data['fname'])
            new_user.second_name = str(form.cleaned_data['sname'])
            new_user.email_address = str(form.cleaned_data['email'])
            if(MyUser.objects.filter(username = new_user.username).count()==1):
                return render(request,'chat/signup.html',{'form':form})
            else:
                new_user.save()
                return HttpResponseRedirect('/')
        return render(request,'chat/signup.html',{'form':form})

class FriendView(View):
    def get(self,request, **kwargs):
        username = kwargs['username']
        form = AddFriendForm(request.POST)
        user = MyUser.objects.get(username=username)
        friends_list = user.friend_list[1:len(user.friend_list)-1].split(',')
        print(friends_list)
        print("\n\n")
        if friends_list[0]=='' :
            friends_list = []
        context = {'flist':friends_list,'username':username,'form':form}
        return render(request,'chat/friends.html',context)
    def post(self,request, **kwargs):
        username = kwargs['username']
        form = AddFriendForm(request.POST)
        user = kwargs['username']
        myuser = MyUser.objects.get(username=username)
        friends_list = (myuser.friend_list)[1:len(myuser.friend_list)-1:].split(',')
        if form.is_valid():
            friend_name=str(form.cleaned_data['username'])
            friend = MyUser.objects.get(username=friend_name)
            if friend in friends_list:
                return render(request,'chat/friends.html',context)
            else:
                myuser.add_friend(friend_name)
                friend.add_friend(username)
                return render(request,'chat/friends.html',context)
        return render(request,'chat/friends.html',{'flist':[username]})


