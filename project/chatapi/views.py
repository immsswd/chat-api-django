from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Chat
from .serializers import ChatSerializer

# Create your views here.
class ChatList(generics.ListCreateAPIView):
    # get data from which model
    queryset            = Chat.objects.all()
    # what Serializer we're going to use for this view
    serializer_class    = ChatSerializer
    # permission just for authenticated user can do something with the endpoint
    permission_classes  = [permissions.IsAuthenticated]
    
    
    # def perform_create: this function name will be call before trying to save data into DB
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
