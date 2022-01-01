from django.urls import path
from . import views

urlpatterns = [
    path("", views.stc),
    path("add_stc", views.add_stc),
    path("delete/<int:id>", views.delete),
    path("edit_stc/<int:id>", views.edit),
]
