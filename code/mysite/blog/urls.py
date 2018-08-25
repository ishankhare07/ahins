from django.conf.urls import url
from django.shortcuts import render
from blog import views

urlpatterns = [
    url(r'^$', views.PublishedPostsList.as_view()),
    url(r'^about/$', lambda request: render(request, 'about.html')),
    url(r'^resume.pdf$', lambda request: render(request, 'resume.pdf')),
    url(r'^compose/(?P<post_id>\d+)/$', views.ComposeView.as_view()),
    url(r'^compose/(?P<post_id>\d+)/preview/$', views.PreviewView.as_view()),
    url(r'^posts/list/$', views.PostsList.as_view()),
    url(r'^posts/(?P<post_id>\d+)/$', views.DetailedPost.as_view()),
    url(r'^posts/preview/(?P<post_id>\d+)/$', views.DetailedPreview.as_view()),
    url(r'^compose/new/$', views.ComposeNewBlogPost.as_view()),
    url(r'^posts/images/(?P<post_id>\d+)/$', views.ImageList.as_view()),
    url(r'^images/(?P<pk>\d+)/$', views.ImageUploadView.as_view()),
        ]
