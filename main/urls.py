from django.urls import path
from main.views import index, signup


urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup, name='signup')
]
