from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:topic>",views.topic, name="topic"),
    path("new_page/", views.new_page, name="new_page"),
    path("edit_page/<str:topic>", views.edit_page, name="edit_page")
]
