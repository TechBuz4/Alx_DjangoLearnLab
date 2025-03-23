from django.urls import path
from .views import register_view, login_view, logout_view, profile_view,profile_update_view
from django.contrib.auth import views as auth_views
from .views import (PostListView, 
                    PostDetailView, PostCreateView, PostUpdateView,
                      PostDeleteView, CommentCreateView, CommentUpdateView,
                        CommentDeleteView,
                        search_posts, posts_by_tag,
                        PostByTagListView)


urlpatterns = [
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("profile/", profile_view, name="profile"),
    path("profile/update/", profile_update_view, name="profile_update"),
    path('', PostListView.as_view(), name='post-list'),  # Home page, listing all posts
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # View single post
    path('post/new/', PostCreateView.as_view(), name='post-create'),  # Create new post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # Edit post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  # Delete post
    path('post/<int:post_id>/comment/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/',CommentDeleteView.as_view(), name='comment-delete'),
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('search/', search_posts, name='search'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='post_by_tag'),

]