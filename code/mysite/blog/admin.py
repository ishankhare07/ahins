from django.contrib import admin
from blog.models import BlogPost, Images


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'published_on', 'last_modified', 'publisher')
    readonly_fields = ('last_modified',)


class ImagesAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Images, ImagesAdmin)
