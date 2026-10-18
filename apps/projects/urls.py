from django.urls import path

from .views import project_detail_view, project_list_view

app_name = "projects"

urlpatterns = [
    path("", project_list_view, name="list"),
    path("<slug:slug>/", project_detail_view, name="detail"),
]
