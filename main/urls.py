from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from main.views import index, signup


urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup, name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(template_name='main/login.html'), name='login')
]
