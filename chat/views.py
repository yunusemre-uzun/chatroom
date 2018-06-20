from django.shortcuts import render
import datetime
import time

from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.views import View
from chat.models import Message

'''
#Gecici deneme classi
class Message:
    def __init__(self,messageText,userName,sendingTime):
        self.messageText = messageText
        self.userName = userName
        self.sendingTime = sendingTime
messages =['Hi','Hello','How are you','Fine,thanks','And you?','Thank you']
m1 = Message(messages[0],'user1',time.asctime( time.localtime(time.time())))
time.sleep(1)
m2 = Message(messages[1],'user2',time.asctime( time.localtime(time.time())))
time.sleep(1)
m3 = Message(messages[2],'user1',time.asctime( time.localtime(time.time())))
time.sleep(1)
m4 = Message(messages[3],'user2',time.asctime( time.localtime(time.time())))
time.sleep(1)
m5 = Message(messages[4],'user2',time.asctime( time.localtime(time.time())))
time.sleep(1)
m6 = Message(messages[5],'user1',time.asctime( time.localtime(time.time())))
messageList = [m1,m2,m3,m4,m5,m6]
####
'''
from .models import Message,User
from .forms import MessageForm

class IndexView(View):
    def get(self,request):
        return render(request,'chat/index.html',{})

class ChatView(View):

    def get(self,request):
        messageList = Message.objects.order_by('-date')
        context = {'roomName':'1' , 'messageList':messageList[::-1]}
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
