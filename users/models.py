import uuid
from django.db import models
from posts.models import Post


class User(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254, blank=True)
    posts = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='user_posts')

    def __str__(self):
        return self.name

