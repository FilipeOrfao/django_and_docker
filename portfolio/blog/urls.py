from django.urls import path
from blog import views

app_name = "blog"

urlpatterns = [
    path("", views.blog_index, name="all_blogs"),
    path("post/<int:pk>/", views.blog_detail, name="blog_detail"),
    path("category/<str:category>", views.blog_category, name="blog_category"),
]
