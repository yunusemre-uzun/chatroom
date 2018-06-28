from django.utils import timezone
from chat.models import *
from django.db.models import Q
from django.http import HttpResponse

from chat.models import Message, MyUser
from django import template

register = template.Library()


@register.simple_tag
def getMessages(username,receiver_name):
    user = MyUser.objects.get(username=username)
    print("Receiver name:",receiver_name)
    receiver = MyUser.objects.get(username = '345')
    message_list = Message.objects.filter(
        Q(sender=user.id, receiver=receiver.id) | Q(sender=receiver.id, receiver=user.id)).order_by('-date')[::-1]
    message_list=message_list[:30]
    return message_list



def refreshmessages(user_id,receiver_id):
    new_request = timezone.now()
    user = MyUser.objects.get(id=user_id)
    last_request = user.last_request
    user.last_request = new_request
    message_list = Message.objects.filter(
        Q(sender=user_id, receiver=receiver_id) | Q(sender=receiver_id, receiver=user_id)).order_by('-date')
    latest_message = message_list[0]
    if not(latest_message.date<new_request and latest_message.date>last_request):
            return []
    return_message_list = []
    for message in message_list:
        if(message.date<new_request and message.date>last_request):
            return_message_list.append(latest_message)
        else:
            break
    return return_message_list[::-1]

