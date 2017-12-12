from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
        url(r'^login/$', auth_views.login, name="login", kwargs={'redirect_authenticated_user': True}),
        url(r'^logout/$', auth_views.logout, name="logout")
        ]
