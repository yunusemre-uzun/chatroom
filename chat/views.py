from django.shortcuts import render
import datetime
import time

from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.views import View
from .models import Message,User
from .forms import MessageForm

class IndexView(View):
    def get(self,request):
        return render(request,'chat/index.html',{})

class ChatView(View):

    def get(self,request):
        message_list = list(Message.objects.all())
        form = MessageForm()
        context = {'roomName':'1','messageList':message_list,'form':form}
        return render(request,'chat/chatroom.html',context)

    def post(self, request):
        form = MessageForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            #print message.cleaned_data['my_form_field_name']
            print("\nsdkjakjldsk\n")
            new_message = form.cleaned_data['new_message']
            message_object = Message(text=new_message,date=timezone.now())
            message_object.save()
            HttpResponseRedirect('/chat/') # Redirect after POST
        #return render(request,'/chat/',)
        return self.get(request)
