from django.urls import path
from blog import views

app_name = "blog"

urlpatterns = [
    path("", views.blog_index, name="all_blogs"),
    path("see_request/", views.see_request, name="see_request"),
    path("user_info/", views.user_info, name="user_info"),
    path("post/<int:pk>/", views.blog_detail, name="blog_detail"),
    path("category/<str:category>/", views.blog_category, name="blog_category"),
    path("private_place/", views.private_place, name="private_place"),
    path("staff_place/", views.staff_place, name="staff_place"),
    path("add_messages/", views.add_messages),
]
