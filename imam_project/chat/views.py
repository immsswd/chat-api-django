from django.shortcuts import render, redirect

# Create your views here.
def chat_page(request,  *args, **kwargs):
    context = {'test':'atest'}
    return render(request, "chat/index.html", context)

