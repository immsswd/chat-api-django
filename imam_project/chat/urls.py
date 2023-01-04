from django.urls import path,reverse
from . views import chat_page
# from django.contrib.auth.views import LoginView, LogoutView

app_name = 'chat'

urlpatterns = [
    # display your chat page first
    path("", chat_page, name='chat-main-page'),
    
    # login
    # path("auth/login", LoginView.as_view(template_name ="chat/login.html"), name="login"),
    # path("auth/logout", LogoutView.as_view(), name="logout"),
]
