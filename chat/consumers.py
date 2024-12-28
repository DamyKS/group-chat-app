import json
from channels.generic.websocket import  AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from . models import Chat, Message
from django.contrib.auth.models import User

class ChatRoomConsumer(AsyncWebsocketConsumer):   
    @database_sync_to_async
    def save_message(self, username, message):
        #get the sender 
        sender=User.objects.get(username=username)
        #get the chat
        chat_room_name= self.scope['url_route']['kwargs']['room_name']
        chat = Chat.objects.get(chat_name=chat_room_name)
        #create new message and add a sender and content to it 
        new_message= Message()
        new_message.sender = sender
        new_message.content=message
        new_message.save()
        #add new message to current chat and save
        chat.messages.add(new_message)
        chat.save()
        





    async def connect(self):      
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        
        await self.channel_layer.group_add(
            self.room_group_name,  
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,  
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['username']
        await self.save_message(username,message)

        await self.channel_layer.group_send(
            self.room_group_name,  
            {
                'type':'chatroom_message',
                'message': message,
                'username':username,

            }
        )
    
    async def chatroom_message(self, event):
        message = event['message']
        username = event['username']
        await self.send(text_data=json.dumps({
            'message': message,
            'username':username,
        }))


