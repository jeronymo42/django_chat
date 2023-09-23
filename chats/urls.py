from django.urls import path
from chats.views import index, chat


urlpatterns = [
    path('', index, name='chats'),
    path('<slug:slug>/', chat, name='chat'),
]
