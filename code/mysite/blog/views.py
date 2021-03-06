import json
import mistune
import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseForbidden
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from blog.serializers import BlogPostSerializer, ImagesUploadSerializer, TagsSerializer, BlogTagsSerializer
from blog.models import BlogPost, Images, Tags
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html


class ImageList(generics.ListCreateAPIView):
    serializer_class = ImagesUploadSerializer

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        return Images.objects.all().filter(post_id=post_id)


class ImageUploadView(generics.RetrieveUpdateAPIView):
    queryset = Images.objects.all()
    serializer_class = ImagesUploadSerializer

    def perform_create(self, serializer):
        img_name = serializer.data.name
        serializer.data.name = img_name.split('?')[0]

        url = serializer.data.image
        serializer.data.image = url.split('?')[0]
        serializer.save()

class TagsView(generics.ListCreateAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer


class BlogTagsView(generics.RetrieveUpdateAPIView):
    serializer_class = BlogTagsSerializer

    def get_queryset(self):
        post_id = self.kwargs.get('pk')
        return BlogPost.objects.filter(id=post_id)


@method_decorator(login_required, name='dispatch')
@method_decorator(ensure_csrf_cookie, name='get')
class ComposeView(View):
    def get(self, request, post_id):
        bp = BlogPost.objects.get(id=post_id)
        return render(request, 'compose/index.html', {'title': bp.title,
                                                    'content': bp.content,
                                                    'id': bp.id,
                                                    'background_image': bp.background_image})

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
    def limit_published(self, bp):
        return not bp.is_published

    def get(self, request, post_id):
        bp = BlogPost.objects.get(id=post_id)
        if self.limit_published(bp):
            return HttpResponseForbidden()
        renderer = MarkdownRenderer()
        markdown_parser = mistune.Markdown(renderer=renderer)
        md = markdown_parser(bp.content)
        return render(request, 'posts/detailed_post.html', {'content': md,
                                                            'title': bp.title,
                                                            'published_on': bp.published_on,
                                                            'summary': bp.summary,
                                                            'tags': bp.tags.all(),
                                                            'background_image': bp.background_image})


@method_decorator(login_required, name='dispatch')
class DetailedPreview(DetailedPost):
    def limit_published(self, bp):
        return False


@method_decorator(login_required, name='dispatch')
class PostsList(ListView):
    model = BlogPost
    template_name = 'posts/list.html'


class PublishedPostsList(ListView):
    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True).order_by('-published_on')

    def get_context_object_name(self, object_list):
        return 'published_posts'

    def get_context_data(self, **kwargs):
        ctx_data = ListView.get_context_data(self, **kwargs)
        ctx_data['title'] = 'Home'
        return ctx_data

    template_name = 'index.html'
