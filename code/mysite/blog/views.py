import json
import mistune
import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from blog.serializers import BlogPostSerializer, ImagesUploadSerializer
from blog.models import BlogPost, Images
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html


def index(request):
    return render(request, 'index.html', {'title': 'Home'})


class ImageList(generics.ListCreateAPIView):
    serializer_class = ImagesUploadSerializer

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        return Images.objects.all().filter(post_id=post_id)


class ImageUploadView(generics.RetrieveUpdateAPIView):
    queryset = Images.objects.all()
    serializer_class = ImagesUploadSerializer


@method_decorator(login_required, name='dispatch')
@method_decorator(ensure_csrf_cookie, name='get')
class ComposeView(View):
    def get(self, request, post_id):
        bp = BlogPost.objects.get(id=post_id)
        return render(request, 'compose/index.html', {'title': bp.title, 'content': bp.content, 'id': bp.id})

    def post(self, request, post_id):
        bp = BlogPost.objects.get(id=post_id)
        bp.is_published = True
        bp.published_on = datetime.date.today()
        bp.save()
        return HttpResponseRedirect('/posts/{0}/'.format(bp.id))

    def put(self, request, post_id):
        bp = BlogPost.objects.get(id=post_id)
        data = json.loads(request.body)
        serializer = BlogPostSerializer(bp, data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

class MarkdownRenderer(mistune.Renderer):
    """
        This custom renderer overrides the default behavior for code blocks
        and for images (with future support for other media types like video).
        Images will be given a css class for making them responsive.
    """

    def block_code(self, code, lang):
        if not lang:
            return '\n<pre><code>{0}</code></pre>\n'.format(mistune.escape(code))
        lexer = get_lexer_by_name(lang)
        formatter = html.HtmlFormatter(cssclass='ahins')
        return highlight(code, lexer, formatter)

    def image(self, src, title, text):
        return '<img src={0} class="responsive-img" title="{1}" alt="{2}">'.format(src, title, text)


@method_decorator(login_required, name='dispatch')
class PreviewView(View):
    def get(self, request, post_id):
        bp = BlogPost.objects.get(id=post_id)
        renderer = MarkdownRenderer()
        markdown_parser = mistune.Markdown(renderer=renderer)
        md = markdown_parser(bp.content)
        return render(request, 'compose/preview.html', {'content': md})

@method_decorator(login_required, name='dispatch')
class ComposeNewBlogPost(View):
    def post(self, request):
        post = BlogPost.objects.create(publisher=request.user)
        return HttpResponseRedirect('/compose/{0}'.format(post.id))


class DetailedPost(View):
    def get(self, request, post_id):
        bp = BlogPost.objects.get(id=post_id)
        renderer = MarkdownRenderer()
        markdown_parser = mistune.Markdown(renderer=renderer)
        md = markdown_parser(bp.content)
        return render(request, 'posts/detailed_post.html', {'content': md, 'title': bp.title, 'published_on': bp.published_on, 'summary': bp.summary})


class PostsList(ListView):
    model = BlogPost
    template_name = 'posts/list.html'
