from django.urls import path
from .views import *

urlpatterns = [
    path("projects/", projects, name="projects"),
    path("<uuid:id>/", get_project, name="project"),
    path("add/", project_add, name="add_project"),
    path("edit/<uuid:id>/", edit_project, name="edit_project"),
    path("delete/<uuid:id>/", delete_project, name="delete_project"),
    path("comment/delete/<int:comment_id>/", delete_comment, name="delete_comment"),
]
