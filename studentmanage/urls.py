from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_list),
    path("add_list/", views.add_list),
    path("delete/<int:id>", views.delete),
    path("edit/<int:id>", views.edit),
]
