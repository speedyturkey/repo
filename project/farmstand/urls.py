from django.conf.urls import patterns, url
from farmstand import views

urlpatterns = patterns('',
	url(r'^$', views.home, name='home'),
    url(r'^products/$', views.products, name='products'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^weekly_products/$', views.weekly_products, name='weekly_products'),
	url(r'^season_select/$', views.season_select, name='season_select'),
	url(r'^inline_test/$', views.inline_test, name='inline_test'),
	url(r'^get_season_weeks/$', views.get_season_weeks, name='get_season_weeks'),
)
