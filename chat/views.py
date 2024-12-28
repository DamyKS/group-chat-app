from django.shortcuts import render
from . models import Chat, Message
from django.contrib.auth.decorators import login_required


def index(request):
    chats = Chat.objects.all()
    context= {
        'chats':chats,
    }
    return render(request, 'index.html', context)
@login_required
def room(request,room_name):
    try:
        chat = Chat.objects.get(chat_name=room_name)
    except Chat.DoesNotExist:
        new_chat= Chat()
        new_chat.chat_name= room_name
        new_chat.save()
        chat=new_chat

    messages = chat.messages.order_by('timestamp').all()
    return render(request, 'chatroom.html', {
        'room_name': room_name,
        'messages':messages,
        #'request':request
    })

