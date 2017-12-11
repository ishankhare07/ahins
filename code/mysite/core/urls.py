from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
        url(r'^login/$', auth_views.login, kwargs={'redirect_authenticated_user': True})
        ]
