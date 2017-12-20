from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from blog.models import BlogPost

# Create your views here.

def index(request):
    return render(request, 'index.html', {'title': 'Home'})


@method_decorator(login_required, name='dispatch')
class ComposeView(View):
    def get(self, request, post_id):
        bp = BlogPost.objects.get(id=post_id)
        return render(request, 'compose/index.html', {'title': bp.title, 'content': bp.content})

    def post(self, request):
        if request.type == 'new_blog_post':
            return HttpResponse('ack create new blog post')
        return HttpResponse('success')


@method_decorator(login_required, name='dispatch')
class ComposeNewBlogPost(View):
    def post(self, request):
        post = BlogPost.objects.create(publisher=request.user)
        return HttpResponseRedirect('/compose/{0}'.format(post.id))

class PostsList(ListView):
    model = BlogPost
    template_name = 'posts/list.html'
