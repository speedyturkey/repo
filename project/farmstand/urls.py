from django.conf.urls import patterns, url
from farmstand import views

urlpatterns = patterns('',
	url(r'^$', views.home, name='home'),
    url(r'^products/$', views.products, name='products'),
    url(r'^register/$', views.register, name='register'),
)