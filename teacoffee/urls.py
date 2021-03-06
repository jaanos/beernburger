from django.conf.urls import url
from . import views

app_name = 'teacoffee'

urlpatterns = [
	# /teacoffee/
	url(r'^$', views.index, name="index"),
	
	# /teacoffee/<torc_id>/
	url(r'^review/(?P<torc_id>[0-9]+)/$', views.detail, name="detail"),

	# /teacoffee/search=<query>/
	url(r'^search=(?P<query>[\s\S]+)/$', views.search, name="search"),
	
	# /teacoffee/sort=<sort_by>/
	url(r'sort=(?P<sort_by>[\s\S]+)/$', views.index, name='sort'),

	# /teacoffe/browse=maker/for=<item>/
        url(r'browse=maker/for=(?P<item>[\s\S]+)/$', views.browse_item, name='browse_item'),

        # /teacoffee/browse=maker/
        url(r'browse=maker/$', views.browse, name='browse'),
]
