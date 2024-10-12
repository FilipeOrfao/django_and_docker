from django.urls import path
from users import views

app_name = "users"

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("register/", views.register, name="register"),
]
