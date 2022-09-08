from django.shortcuts import render
from .models import Service
from django.core.urlresolvers import reverse

# Create your views here.

def all_services(request):
	all_service = Services.objects.all()
	template = 'services/all_servcies.html'
	context = {'all_service':all_service}
	return render(request, template, context)

def single_service(request, slug):
	single = Service.objects.get(slug = slug)
	template = 'service/single_service.html'
	context = {'single_service' : single}
	return render(request, template, context)

def all_departments(request):
	all_service = Services.objects.all()
	template = 'services/all_servcies.html'
	context = {'all_service':all_service}
	return render(request, template, context)

def single_department(request, slug):
	single = Service.objects.get(slug = slug)
	template = 'service/single_service.html'
	context = {'single_service' : single}
	return render(request, template, context)

def all_portfolio(request):
	all_portfolio = Portfolio.objects.all()
	template = 'portfolio.all_portfolio.html'
	context = {'all_portfolio' : all_portfolio}
	return render(request, template, context)

def single_portfolio(request, id):
	single = Portfolio.pbjects.get(id = id)
	template = 'portfolio/single_portfolio.html'
	context = {'all_portfolio' : all_portfolio}
	return render(request, template, context)

def index(request):
	context ={'page_name' : 'Home' }
	template = 'index.html'
	return render(request, template, context)

def about(request):
	about_page = reverse('about')
	context ={'urls': [about_page], 'page_name' : 'About' }
	template = 'about.html'
	return render(request, template, context)

def contact(request):
	contact_page = reverse('contact')
	context ={'urls': [contact_page], 'page_name' : 'Contact' }
	template = 'contact.html'
	return render(request, template, context)



	