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
            if(password==u.password):
                return HttpResponseRedirect(username+'/chat')
            else:
                return IndexView.get()
        return
    def get(self,request):
        return HttpResponse("get Username View")

class SignUpView(View):
    def get(self,request):
        form = SignUpForm()
        return render(request,'chat/signup.html',{'form':form})

    def post(self):
        print("\nsakdlsad\n")
        sign_up_form = SignUpForm(request.POST)
        if sign_up_form.is_valid():
            username = str(sign_up_form.cleaned_data['username'])
            password = str(sign_up_form.cleaned_data['password'])
            first_name = str(sign_up_form.cleaned_data['fname'])
            second_name = str(sign_up_form.cleaned_data['sname'])
            email_address = str(sign_up_form.cleaned_data['email'])
            if(MyUser.objects.filter(username = username).count()==1):
                return
            else:
                new_user = MyUser(username=username,password=password,first_name=first_name,last_name=second_name,email=email_address)
                new_user.save()
                return render(request,'chat/signup.html',{'form'})
        return
