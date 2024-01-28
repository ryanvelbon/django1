from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    path("", views.post_index, name="post_index"),
    path("<int:id>", views.post_show, name="post_show"),
]