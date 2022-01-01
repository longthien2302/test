from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_absent),
    path("add_absent/", views.add_absent),
    path("delete/<int:id>", views.delete),
    path("edit/<int:id>", views.edit),
]
