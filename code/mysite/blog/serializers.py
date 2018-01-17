from core.models import User
from blog.models import BlogPost, Images
from rest_framework import serializers


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'


class ImagesUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'
