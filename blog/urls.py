from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^post_list/$', views.post_list, name='post_list'),
    url(r'^search_list/$', views.search_list, name='search_list'),
    url(r'^sign_up/$', views.sign_up, name='sign_up'),
    url(r'^blog_search_list_view/$', views.blog_search_list_view, name='blog_search_list_view'),
    url(r'^sign_up/process.php$', views.process, name='process'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^$', views.title_page, name='title_page'),
    url(r'^post/(?P<pk>\d+)/delete/$', views.PostDelete.as_view(), name='post_delete')
]
