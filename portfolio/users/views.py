from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse
from users.forms import CustomeUserCreationFrom


# Create your views here.
def dashboard(request):

    return render(request, "users/dashboard.html")


def register(request):

    if request.method == "GET":
        return render(
            request,
            "users/register.html",
            {"form": CustomeUserCreationFrom},
        )
    elif request.method == "POST":
        form = CustomeUserCreationFrom(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.backend = "django.contrib.auth.backends.ModelBackend"
            user.save()
            login(request, user)
            return redirect(reverse("users/dashboard.html"))
