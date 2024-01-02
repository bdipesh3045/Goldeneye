from django.contrib import admin
from blog.models import Category, Comment, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "post_titles"]
    list_per_page = 10

    def post_titles(self, obj):
        return ", ".join(post.title for post in obj.posts.all())

    post_titles.short_description = "Post Titles"


class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "last_modified", "display_categories", "created_on"]
    list_per_page = 10

    def display_categories(self, obj):
        return ", ".join(category.name for category in obj.categories.all())

    display_categories.short_description = "Categories"


class CommentAdmin(admin.ModelAdmin):
    list_display = ["author", "post_blog", "body", "created_on"]
    list_per_page = 10

    def post_blog(self, obj):
        return obj.post.title

    post_blog.short_description = "Blog Title"


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
