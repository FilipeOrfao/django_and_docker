from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from blog.models import Post, Comment
from blog.forms import CommentForm


# Create your views here.


def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {"posts": posts}

    return render(request, "blog/index.html", context)


def blog_category(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by(
        "-created_on"
    )
    context = {"category": category, "posts": posts}

    return render(request, "blog/category.html", context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": CommentForm(),
    }
    return render(request, "blog/detail.html", context)


def see_request(request):

    text = f"""
        "scheme": {request.scheme},
        "path": {request.path},
        "method": {request.method},
        "GET": {request.GET},
        "user": {request.user},
        """

    return HttpResponse(text, content_type="text/plain")


def user_info(request):
    text = f"""
        Selected HttpRequest.user attributes:
        username: {request.user.username}
        is_anonymous: {request.user.is_anonymous}
        is_staff: {request.user.is_staff}
        is_superuser: {request.user.is_superuser}
        is_active: {request.user.is_active}
        """

    return HttpResponse(text, content_type="text/plain")


@login_required
def private_place(request):
    return HttpResponse("shh, members only!", content_type="text/plain")


@user_passes_test(lambda user: user.is_staff)
def staff_place(request):
    return HttpResponse("you are a staff", content_type="text/plain")


@login_required
def add_messages(request):
    username = request.user.username
    messages.add_message(request, messages.INFO, f"Hello {username}")
    messages.add_message(request, messages.WARNING, f"DANGER WILL ROBINSON!")
    return HttpResponse("Message Added", content_type="text/pain")
