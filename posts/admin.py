from django.contrib import admin
from posts.models import Author, Comment, Post


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(Post, PostAdmin)
