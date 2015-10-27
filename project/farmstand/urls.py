from django.conf.urls import patterns, url
from farmstand import views

urlpatterns = patterns('',
	url(r'^$', views.home, name='home'),
    url(r'^products/$', views.products, name='products'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
)