import uuid
from django.template.defaultfilters import slugify
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class Author(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    fname = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.fname


class Post(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50, null=False, blank=False)
    slug = models.SlugField(null=False, unique=True)
    category = models.ManyToManyField('Tag', related_name='category', blank=True)
    body = RichTextField()
    creator = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    comment_text = models.TextField(max_length=200)
    comment_time = models.DateTimeField(auto_now_add=True)
    comment_update_time = models.DateTimeField(auto_now=True)
    comment_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.comment_text} by {self.comment_by}'


class Tag(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name
