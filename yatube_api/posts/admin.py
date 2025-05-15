from django.contrib import admin

from posts.models import Comment, Follow, Group, Post


admin.site.empty_value_display = "-пусто-"


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("pk", "text", "pub_date", "author")
    search_fields = ("text",)
    list_filter = ("pub_date",)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "slug")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("pk", "post", "author", "text", "created")


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ("user", "following")
