from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from chats.models import Chat, Message

# Create your views here.

@login_required
def index(request):
    chats = Chat.objects.all()
    return render(request, 'chats/chats.html', {'chats': chats})

@login_required
def chat(request, slug):
    if request.method == "POST":
        chat = Chat.objects.get(slug=slug)
        user = User.objects.get(username=request.user.username)
        Message.objects.create(chat=chat, user=user, content=request.POST['message'])
        return redirect('chat', slug)
    chat = Chat.objects.get(slug=slug)
    messages = Message.objects.filter(chat=chat).order_by('-pk')[0:10][::-1]
    return render(request, 'chats/chat.html', {'chat': chat, 'messages': messages})