from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Chat(models.Model):
    name = models.CharField('Название', max_length=255)
    slug = models.SlugField('URI', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Название чата"
        verbose_name_plural = "Названия чатов"


class Message(models.Model):
    chat = models.ForeignKey(Chat, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        ordering = ('date_added',)