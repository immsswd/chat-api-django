from django.urls import path
from . import views

urlpatterns = [
    path('', views.getMyData),
    path('add-msg/', views.addData)
]
