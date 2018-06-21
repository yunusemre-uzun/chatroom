from  django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
import datetime
import time

from django.http import HttpResponse, HttpResponseRedirect, request
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.views import View
from .models import Message, MyUser
from .forms import MessageForm, UserForm,SignUpForm


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
            password = str(form.cleaned_data['password'])
            try:
                MyUser.objects.get(username=username)
            except:
                MyUser.DoesNotExist()
            u = MyUser.objects.get(username=username)
            if(u.check_password(password)):
                return HttpResponseRedirect(username+'/chat')
            else:
                return IndexView.get()


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
            if(MyUser.objects.filter(username__lte = new_user.username).count()==1):
                return HttpResponseRedirect('/error')
            else:
                new_user.save()
                return HttpResponseRedirect('/')
        return render(request,'chat/signup.html',{'form':form})
