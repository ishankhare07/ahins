from django.contrib import admin
from blog.models import BlogPost, Images, Tags, BlogTags


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'published_on', 'last_modified', 'publisher')
    readonly_fields = ('last_modified',)
    filter_horizontal = ('tags',)


class BlogTagsAdmin(admin.ModelAdmin):
    list_display = ('blog', 'tag')


class ImagesAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Images, ImagesAdmin)
admin.site.register(Tags, admin.ModelAdmin)
admin.site.register(BlogTags, BlogTagsAdmin)
