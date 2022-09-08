from django.db import models
from services.models import Timestamp
from django.core.urlresolvers import reverse
from django.conf import settings
from services.models import Tag

# Create your models here.

class Post(Timestamp):
	title = models.CharField(max_length=20)
	content = models.TextField()
	image = models.ImageField(upload_to = 'blog/pictures')
	author = models.ForeignKey(settings.AUTH_USER_MODEL, default = 'Boiyelabs')
	tags = models.ManyToManyField('Tags')


	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post_detail', kwargs={'slug':self.slug})


class Coments(Timestamp):
	content = models.TextField()