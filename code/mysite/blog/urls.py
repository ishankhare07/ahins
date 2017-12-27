from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^compose/(?P<post_id>\d+)/$', views.ComposeView.as_view()),
    url(r'^posts/list/$', views.PostsList.as_view()),
    url(r'^compose/new/$', views.ComposeNewBlogPost.as_view())
        ]
