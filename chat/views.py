from django.shortcuts import render
import datetime
import time

from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
# Create your views here.
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

class IndexView(View):
    def get(self,request):
        return render(request,'chat/index.html',{})

class ChatView(View):

    def get(self,request):

        messageList = Message.objects.order_by('-date')
        context = {'roomName':'1' , 'messageList':messageList[::-1]}
        return render(request,'chat/chatroom.html',context)

    def post(self, request):
        return
