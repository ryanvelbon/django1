from django.urls import path
from . import views

app_name = "shop"
urlpatterns = [
    path("", views.product_index, name="product_index"),
    path("<int:id>", views.product_show, name="product_show"),
]