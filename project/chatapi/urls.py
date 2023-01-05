from django.urls import path
from .views import ChatList

urlpatterns = [
    path("", ChatList.as_view(), name='chat_list'),
]
