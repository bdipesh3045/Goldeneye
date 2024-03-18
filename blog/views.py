from django.http import HttpResponseRedirect
from django.shortcuts import render

from blog.forms import CommentForm
from blog.models import Comment, Post


def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {"posts": posts, "News": "False"}
    return render(request, "index_blog.html", context)


def blog_category(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by(
        "-created_on"
    )
    context = {"category": category, "posts": posts, "News": "True"}
    return render(request, "category.html", context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)

        comment = Comment(
            author=request.user.username,
            body=request.POST.get("message"),
            post=post,
        )
        comment.save()
        return HttpResponseRedirect(request.path_info)
    comments = Comment.objects.filter(post=post)
    context = {"post": post, "comments": comments, "form": form}

    return render(request, "detail.html", context)
