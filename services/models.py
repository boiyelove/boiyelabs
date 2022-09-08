import datetime
from django.utils import timezone
from django.db import models

# Create your models here.

class Timestamp(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	edited_at = models.DateTimeField(auto_now=True)
	published_at = models.DateTimeField()
	active = models.BooleanField(default = False)
	featured = models.BooleanField(default = False)

	def limit_pub_date_choices():
		return {'pub_date__lte': datetime.date.ustcnow()}

	def was_published_recently(self):
		return now -datetime.tiumedelta(days=1) <= self.pub_date <= now
	was_published_recently.admin_order_field = 'published_at'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published_recently'


class Catalog(models.Model):
	name = models.CharField(max_length = 30)
	parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank = True, null = True)

	def __str__(self):
		return self.name

class Service(Timestamp):
	name = models.CharField(max_length = 35)
	catalog = models.ForeignKey(Catalog, on_delete=models.SET_NULL, blank=True, null=True)

	def __str__(self):
		return self.name

class Tag(models.Model):
	name = models.CharField(max_length = 15)
	services = models.ManyToManyField(Service)
	def __str__(self):
		return  self.name

class Portfolio(Timestamp):
	name = models.CharField(max_length = 15)
	addr = models.URLField()
	customer = models.CharField(max_length = 12)
	doc = models.FileField(upload_to = 'services/portfolio')

	def __str__(self):
		return self.name
