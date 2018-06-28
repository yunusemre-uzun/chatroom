from django.db.models import Q

from chat.models import Message


def getMessages(user_id,receiver_id):
    message_list = Message.objects.filter(
        Q(sender=user_id, receiver=receiver_id) | Q(sender=receiver_id, receiver=user_id)).order_by('-date')[::-1]

    return message_list

