from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^post/(?P<id>[0-9]+)/$', views.post_detail, name='detail'),
    url(r'^post/new/$', views.post_new, name='new'),
    url(r'^post/(?P<id>[0-9]+)/edit/$', views.post_edit, name='edit'),
    url(r'^draft/$', views.post_draft_list, name='draft'),
    url(r'^post/(?P<id>[0-9]+)/publish/$', views.post_publish, name='publish'),

]
