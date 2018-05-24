from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.flatpages import views as flat_views
from . import views


urlpatterns = [
    url(r'^$', views.post_cat, name='home'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^post_list/$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/(?P<post_slug>[\w\d-]+)$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^about/$', flat_views.flatpage, {'url': '/about/'}, name='about'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
