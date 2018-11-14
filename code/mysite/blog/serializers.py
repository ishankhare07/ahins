from core.models import User
from blog.models import BlogPost, Images, Tags, BlogTags
from rest_framework import serializers


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'


class ImagesUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'


class BlogTagsSerializer(serializers.ModelSerializer):
    tags = TagsSerializer(many=True, read_only=True)
    class Meta:
        model = BlogPost
        fields = '__all__'
