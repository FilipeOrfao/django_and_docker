from django.urls import path
from projects import views

app_name = "projects"

urlpatterns = [
    path("", views.all_projects, name="all_projects"),
    path("test", views.project_list, name="projects_home"),
    path("<int:pk>", views.project_detail, name="project_detail"),
    path("<str:title>", views.project_detail_title, name="project_detail_title"),
]
