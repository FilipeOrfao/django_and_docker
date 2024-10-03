from django.http import HttpResponse
from django.shortcuts import render
from projects.models import Project


# Create your views here.
def project_list(request):
    return render(request, "projects/index.html")


def all_projects(request):
    projects = Project.objects.all()
    return render(request, "projects/all_projects.html", {"projects": projects})
