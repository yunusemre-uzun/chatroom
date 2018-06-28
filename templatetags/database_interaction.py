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

