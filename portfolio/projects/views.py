from django.shortcuts import render
from projects.models import Project


# Create your views here.
def project_list(request):
    return render(request, "projects/index.html")


def all_projects(request):
    projects = Project.objects.all()
    return render(request, "projects/all_projects.html", {"projects": projects})


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, "projects/detail.html", {"project": project})


def project_detail_title(request, title):
    project = Project.objects.get(title=title)
    return render(request, "projects/detail.html", {"project": project})
