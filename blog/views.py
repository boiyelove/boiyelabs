from django.shortcuts import render
from django.views.generic imporpt ListView
from .models import Posts

# Create your views here.

def all_posts(request):
	posts = Posts.objects.all()
	template = 'blog/all_posts.html'
	context = {'post':post}
	return  render(request, template, context)

def single_post(request, slug):
	single_post  = Posts.object.get(slug = slug)
	template = 'blog/single_post.html'
	context = {'single_post':single_post}

	return render(request, template, context)

class PostListView(ListView):
	model = Post
	context_object_name = 'post_list_objects'

	def head(self, *args, *kwargs):
		last_book = self.get_quesryset().latest('publication_date')
		response = HttpResponse('')

		response['Last-Modified']= last_book,publication_date.strftime('%a, %d %b %Y %H: %M:%S GMT')
		return response

class PostDetail(DetailView):
	model = Post
	

	def get_context_data(self, *kwargs):
		context = super(PostDetail, self).get_context_data(**kwargs)
		context'[post_list'] = Posts.objects.all()
		return context

