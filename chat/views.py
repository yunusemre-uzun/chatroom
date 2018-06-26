import json

from  django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.shortcuts import render, redirect
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
        receiver_name = kwargs['receiver']
        user = MyUser.objects.get(username= username)
        receiver = MyUser.objects.get(username = receiver_name)
        #filter(Q(..) | Q(..)) allows the usage of or in filter function
        message_list = Message.objects.filter(Q(sender = user.id,receiver = receiver.id) | Q(sender = receiver.id, receiver = user.id)).order_by('-date')[::-1]
        form = MessageForm()
        context = {'roomName':'','messageList':message_list,'form':form, 'username':username ,'receiver':receiver}
        #change the unread messages status from {{receivername}} to {{username}} in database to read(coming messages)
        change_message_list = list(Message.objects.filter(sender=receiver.id,receiver=user.id,is_read=False))
        print(change_message_list)
        for message in change_message_list:
            message.is_read=True
            message.save()
        user.save()
        ##############################################
        #if (request.is_ajax()): #if the request is ajax, only renders the message part
         #   context = {'messageList': message_list }
          #  return render(request, 'chat/ajaxChatroom.html', context)
        return render(request,'chat/chatroom.html',context)

    def post(self, request, **kwargs):
        username = kwargs['username']
        receiverName = kwargs['receiver']
        form = MessageForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            user = MyUser.objects.get(username=username)
            receiver = MyUser.objects.get(username = receiverName)
            new_message = form.cleaned_data['new_message']
            message_object = Message(text=new_message,sender= user,receiver = receiver ,date=timezone.now())
            message_object.save()
            receiver.save()
            if (request.is_ajax()):  # if the request is ajax, only renders the message part
                return self.get(request , username= username , request= request)
            return HttpResponseRedirect(reverse('chat:friend', args = [username , receiverName]))

class AjaxChatView(View):
    def get(self,request, **kwargs):
        username = kwargs['username']
        receiver_name = kwargs['receiver']
        user = MyUser.objects.get(username= username)
        receiver = MyUser.objects.get(username = receiver_name)
        #filter(Q(..) | Q(..)) allows the usage of or in filter function
        message_list = Message.objects.filter(Q(sender = user.id,receiver = receiver.id) | Q(sender = receiver.id, receiver = user.id)).order_by('-date')[::-1]
        context = {'messageList':message_list}
        #change the unread messages status from {{receivername}} to {{username}} in database to read(coming messages)
        change_message_list = list(Message.objects.filter(sender=receiver.id,receiver=user.id,is_read=False))
        print(change_message_list)
        for message in change_message_list:
            message.is_read=True
            message.save()
        user.save()
        return render(request,'chat/ajaxChatroom.html',context)



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
        receiver = kwargs.get('receiverName' , "None")
        form = AddFriendForm(request.POST)
        user = MyUser.objects.get(username=username)
        friends_list = user.friend_list[1:len(user.friend_list)-1].split(':')
        message_list = Message.objects.filter(Q(sender = user.id) | Q(receiver = user.id)).order_by('-date')[::-1]
        friends_object_list=[]
        if (not friends_list==['']):
            for friend in friends_list:
                friends_object_list.append(MyUser.objects.get(username=friend))
            friends_object_list=list(friends_object_list)
        ret = [] #the list to send html
        if friends_list[0]=='' :
            friends_list = []
        #find the number of unread messages for each friend in friendlist
        unread_message_count_list = []
        for friend in friends_list:
            friend_object = MyUser.objects.get(username=friend)
            unread_message_count_list.append((Message.objects.filter(sender=friend_object.id,receiver=user.id,is_read=False).count()))
        new_messages=0
        number_of_channels = 0
        c_key = 0
        c_person = ''
        for i in unread_message_count_list :
            new_messages += i
            if(i>0):
                number_of_channels += 1
        if(number_of_channels==1):
            c_key = 1
        #create the list of tuples which [(friend_name,unread_message_count)]
        for i in range(len(friends_list)):
            ret.append((friends_object_list[i],unread_message_count_list[i]))
        if(c_key):
            for i in ret :
                if(i[1]>0):
                    c_person = i[0]
        ####################################
        context = {'user':user,'flist':ret,'message_count':unread_message_count_list,'username':username,
                    'form':form,'new_messages':new_messages,'number_of_channels':number_of_channels,
                    'c_key':c_key, 'c_person':c_person,'receiver':receiver}
        return render(request,'chat/friends.html',context)


    def post(self,request, **kwargs):

        form = AddFriendForm(request.POST)
        username = kwargs['username']
        receiver = kwargs.get('receiver', "None")
        myuser = MyUser.objects.get(username=username)
        friends_list = (myuser.friend_list)[1:len(myuser.friend_list)-1:].split(',')
        if form.is_valid():
            friend_name=str(form.cleaned_data['username'])
            friend = MyUser.objects.get(username=friend_name)
            if friend in friends_list:
                return HttpResponseRedirect(reverse('chat:friend', args=[username]))
            else:
                myuser.add_friend(friend_name)
                friend.add_friend(username)
                return HttpResponseRedirect(reverse('chat:friend', args=[username]))
        return render(request,'chat/friends.html',{'flist':[username]})


class FriendView2(View):
    def get(self,request, **kwargs):
        return HttpResponse('2')
