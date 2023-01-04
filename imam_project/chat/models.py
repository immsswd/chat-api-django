from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):
    name        = models.CharField(max_length=40)
    
    def __str__(self):
        return str(self.name)

class Message(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    messages    = models.TextField(null=True)
    created     = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.messages

