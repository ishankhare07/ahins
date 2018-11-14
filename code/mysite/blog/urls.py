from django.conf.urls import url
from django.shortcuts import render
from django.http import HttpResponseRedirect
from blog import views

urlpatterns = [
    url(r'^$', views.PublishedPostsList.as_view()),
    url(r'^about/$', lambda request: render(request, 'about.html')),
    # this should be removed from here, and the link should be updated to the
    # correct path, instead of a useless redirect
    url(r'^resume.pdf$', lambda request: HttpResponseRedirect('/static/resume.pdf')),
    url(r'^compose/(?P<post_id>\d+)/$', views.ComposeView.as_view()),
    url(r'^compose/(?P<post_id>\d+)/preview/$', views.PreviewView.as_view()),
    url(r'^posts/list/$', views.PostsList.as_view()),
    url(r'^posts/(?P<post_id>\d+)/$', views.DetailedPost.as_view()),
    url(r'^posts/preview/(?P<post_id>\d+)/$', views.DetailedPreview.as_view()),
    url(r'^compose/new/$', views.ComposeNewBlogPost.as_view()),
    url(r'^posts/images/(?P<post_id>\d+)/$', views.ImageList.as_view()),
    url(r'^images/(?P<pk>\d+)/$', views.ImageUploadView.as_view()),
    url(r'^tags/$', views.TagsView.as_view()),
    url(r'^posts/(?P<pk>\d+)/tags/$', views.BlogTagsView.as_view()),
        ]
