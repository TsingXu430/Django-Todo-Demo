# coding: utf-8

from django.conf.urls import url
from django.views import static
from views import todo

urlpatterns = [
    url('^$', todo.show),
    url(r'^todo/?$', todo.show),
    url(r'^todo/(?P<status>\d+)', todo.show, name='show'),
    url(r'^todo/add/?$', todo.add, name='add'),
    url(r'^todo/delete/(?P<todo_id>\w+)/(?P<status>\d+)/$', todo.delete, name='delete'),
    url(r'^todo/done/(\w+)/(\d+)/$', todo.done, name='done'),
    url(r'^todo/undone/(?P<todo_id>\w+)/(?P<status>\d+)/$', todo.undone, name='undone'),
    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': 'static'}),
]
