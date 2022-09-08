from django.conf.urls import url
from . import views


urlpatterns = [
url(r'^contact/$', views.contact, name = 'contact'),
url(r'^about/$', views.about, name ='about'),
url(r'^services/$', views.all_services, name ='all_services'),
url(r'^portfolio/$', views.all_portfolio, name ='all_portfolio'),
url(r'^departments/$', views.all_departments, name ='all_departments'),


]