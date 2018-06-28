from django.db.models import Q
from chat.models import Message
from django.utils import timezone
from chat.models import *


def getMessages(user_id,receiver_id):
    message_list = Message.objects.filter(
        Q(sender=user_id, receiver=receiver_id) | Q(sender=receiver_id, receiver=user_id)).order_by('-date')[::-1]

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
    for message in message_list
        if(message.date<new_request and message.date>last_request):
            return_message_list.append(latest_message)
        else:
            break
    return return_message_list[::-1]

