# -*- coding:utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required 
from registration import views
from chat.views import show_chat

urlpatterns = [
    # Examples:
    # url(r'^$', 'private_chat.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^registration/', views.registration, name='reg'),
    url(r'^login/', views.login_view, name='login'),
	url(r'^chat', login_required(show_chat), name='chat'), # если юзер не авторизован отправит на урл в настройках LOGIN_URL
    url(r'^$', views.home, name='index'),

]
