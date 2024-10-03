from django.urls import path
from projects import views

urlpatterns = [
    path("", views.all_projects, name="all_projects"),
    path("test", views.project_list, name="projects_home"),
]
