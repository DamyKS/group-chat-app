from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.username}: {self.content[:20]}"  # Truncate for display


class Chat(models.Model):
    """A model to hold all messages in a chat room"""
    chat_name=models.CharField(max_length=30, blank=True)
    messages=models.ManyToManyField(Message, related_name="messages", blank=True)

    def __str__(self):
        return self.chat_name
    