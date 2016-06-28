from django.conf.urls import include, url
from django.contrib import admin
from registration import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'private_chat.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^registration/', views.registration, name='reg'),
    url(r'^login/', views.login_view, name='login'),
    
]
