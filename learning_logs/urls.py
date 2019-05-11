"""基于logs的urls"""
from django.conf.urls import url
from . import views

app_name = 'learning_logs'
urlpatterns = [
    #主页
    url(r'^$',views.index, name='index'),
    #主题页
    url(r'^topics/$',views.topics, name='topics'),
    #特定主题页
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic , name='topic'),
    #用户添加主题页
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    #用户添加主题内容页
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    #用户编辑已有的主题
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]