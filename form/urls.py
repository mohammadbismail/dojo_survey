from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("input", views.create_users),
    path("result", views.result),
]
