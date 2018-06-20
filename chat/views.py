from django.shortcuts import render
import datetime
import time

from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.views import View
from .models import Message, User
from .forms import MessageForm, UserForm


class IndexView(View):
    def get(self,request):
        form = UserForm()
        return render(request,'chat/index.html',{'form':form})

class ChatView(View):
    def get(self,request, **kwargs):
        username = kwargs['username']
        print(username)
        message_list = Message.objects.order_by('-date')[::-1]
        form = MessageForm()
        context = {'roomName':'1','messageList':message_list,'form':form, 'username':username}
        return render(request,'chat/chatroom.html',context)

    def post(self, request, **kwargs):
        username = kwargs['username']
        form = MessageForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            new_message = form.cleaned_data['new_message']
            message_object = Message(text=new_message,sender= username,date=timezone.now())
            message_object.save()
        return self.get(request, username = username)


class UsernameView(View):
    def post(self,request):
        form = UserForm(request.POST)
        if form.is_valid():
            username = str(form.cleaned_data['username'])
            user = User(nickname= username)
            user.save()
            return HttpResponseRedirect(username+'/chat')
