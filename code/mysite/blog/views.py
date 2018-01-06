import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.views import APIView
from blog.serializers import BlogPostSerializer
from blog.models import BlogPost

# Create your views here.

def index(request):
    return render(request, 'index.html', {'title': 'Home'})


@method_decorator(login_required, name='dispatch')
@method_decorator(ensure_csrf_cookie, name='get')
class ComposeView(View):
    def get(self, request, post_id):
        bp = BlogPost.objects.get(id=post_id)
        return render(request, 'compose/index.html', {'title': bp.title, 'content': bp.content, 'id': bp.id})

    def post(self, request):
        if request.type == 'new_blog_post':
            return HttpResponse('ack create new blog post')
        return HttpResponse('success')

    def put(self, request, post_id):
        bp = BlogPost.objects.get(id=post_id)
        data = json.loads(request.body)
        serializer = BlogPostSerializer(bp, data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

@method_decorator(login_required, name='dispatch')
class PreviewView(APIView):
    def get(self, request, post_id):
        bp = BlogPost.objects.get(id=post_id)
        return HttpResponse([bp.title, bp.content])

@method_decorator(login_required, name='dispatch')
class ComposeNewBlogPost(View):
    def post(self, request):
        post = BlogPost.objects.create(publisher=request.user)
        return HttpResponseRedirect('/compose/{0}'.format(post.id))

class PostsList(ListView):
    model = BlogPost
    template_name = 'posts/list.html'
