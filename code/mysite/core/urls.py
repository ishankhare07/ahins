from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
        url(r'^login/$', auth_views.LoginView, name="login", kwargs={'redirect_authenticated_user': True}),
        url(r'^logout/$', auth_views.LogoutView, name="logout", kwargs={'next_page': '/'})
        ]
