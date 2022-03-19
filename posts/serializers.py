from rest_framework import serializers
from django.contrib.auth.models import User
from posts.models import Author, Comment, Post


class UserMinimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    comment_by = UserMinimalSerializer()

    class Meta:
        model = Comment
        fields = ['id', 'comment_text', 'comment_by', 'comment_time', 'comment_update_time']
        # exclude = ('post',)


class PostSerializer(serializers.ModelSerializer):
    creator = AuthorSerializer()
    comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = ('pk', 'id', 'title', 'slug', 'creator', 'comments', 'created_on')
