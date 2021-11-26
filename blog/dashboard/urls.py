from django.urls import path
from dashboard.views import *

app_name = "dashboard"

urlpatterns = [
    path("Search", Search),
    path("Dashboard", Dashboard),
    path("CreatingPost", CreatePost),
    path("EditingPost/<int:pk>", EditPost, name='editpost'),
    path("DeletingPost/<int:pk>", DeletePost, name='deletepost'),
]