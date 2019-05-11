"""为应用程序users定义URL模式"""

from django.conf.urls import url
from django.contrib.auth.views import LoginView
from . import views

app_name = 'learning_logs'
urlatterns = [
    #登陆界面
    url(r'^login/$', login, {'template_name': 'user/login.html'}, name='login'),
]











