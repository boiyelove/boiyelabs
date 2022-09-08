from django.conf.urls import url
from . import views


urlpattern = [
	url(r'^$', views.all_post, name = 'all_blog_post'),
	url(r'^(?P<slug>[\w+])', views.single_post, name = 'post_detail'),


	]