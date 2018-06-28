from django.http import HttpResponse, HttpResponseRedirect, request
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views import View
from .forms import *
from chat.models import MyUser


def index(request):
    active_user=request.user
    return render(request,'index.html',{'username':active_user.username})

def logout(request):
    HttpResponseRedirect('/accounts/logout/')
    return render(request,'registration/logout.html')

class SignUpView(View):
    def get(self,request):
        form = SignUpForm()
        return render(request,'registration/signup.html',{'form':form})

    def post(self,request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            new_user = MyUser()
            new_user.username = str(form.cleaned_data['username'])
            new_user.set_password(str(form.cleaned_data['password']))
            new_user.first_name = str(form.cleaned_data['fname'])
            new_user.last_name = str(form.cleaned_data['sname'])
            new_user.email_address = str(form.cleaned_data['email'])
            if(User.objects.filter(username = new_user.username).count()==1):
                return render(request,'registration/signup.html',{'form':form})
            else:
                new_user.save()
                return HttpResponseRedirect('/')
        return render(request,'registration/signup.html',{'form':form})

class LogOutView(View):
    def get(self,request):
        return render(request,'registration/logout.html')

