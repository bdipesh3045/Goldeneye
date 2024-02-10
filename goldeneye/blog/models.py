from django.db import models
from ckeditor.fields import RichTextField
import uuid


class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Post(models.Model):
    post_id = models.UUIDField(default=uuid.uuid4, unique=True, null=True)
    title = models.CharField(max_length=255)
    body = RichTextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")
    image = models.ImageField(upload_to="blog/", default="")

    class Meta:
        indexes = [
            models.Index(fields=["model_id"]),
        ]

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_on"]


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} on '{self.post}'"

    class Meta:
        ordering = ["-created_on"]


class Reply(models.Model):

    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    reply = models.TextField()

    def __str__(self):
        return self.reply

    class Meta:
        indexes = [
            models.Index(fields=["name"]),
        ]
        verbose_name = "Reply"
