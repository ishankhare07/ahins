from django.db import models


class BlogPost(models.Model):
    publisher = models.ForeignKey('core.User', on_delete=models.CASCADE)
    background_image = models.TextField(default='//placehold.it/500x200')
    title = models.CharField(max_length=100, null=False, blank=False, default='Untitled')
    is_published = models.BooleanField(default=False)
    published_on = models.DateField(null=True, blank=True)
    last_modified = models.DateTimeField(auto_now=True, blank=False, null=False)
    content = models.TextField(blank=True, null=True, default='')
    summary = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return '{0} {1}'.format(self.id, self.title)


class Tags(models.Model):
    creator = models.ForeignKey('core.User', on_delete=models.CASCADE)
    tag_name = models.TextField(null=False, blank=False)

    def __str__(self):
        return '{}: {}'.format(self.tag_name, self.creator)

    class Meta:
        verbose_name = 'Tag'


class BlogTags(models.Model):
    blog_id = models.ForeignKey('BlogPost', on_delete=models.CASCADE)
    tag_id = models.ForeignKey('Tags', on_delete=models.CASCADE)

    def __str__(self):
        return '{} => {}'.format(self.tag_id.tag_name, self.blog_id.title)

    class Meta:
        verbose_name = 'BlogTag'


class Images(models.Model):
    post_id = models.ForeignKey('blog.BlogPost', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')             # this will require Pillow

    def __str__(self):
        return '{0} {1}'.format(self.id, self.name)

    class Meta:
        verbose_name = 'Image'
