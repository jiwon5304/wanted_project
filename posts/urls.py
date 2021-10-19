from django.urls import path
from .views import PostDetailView, PostListView, PostUpdateView, PostDeleteView


urlpatterns = [
    path("/postdetail", PostDetailView.as_view()),
    path("", PostListView.as_view()),
    path("/postupdate", PostUpdateView.as_view()),
    path("/postdelete/<int:post_id>", PostDeleteView.as_view()),
]