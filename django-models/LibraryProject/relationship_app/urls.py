from django.urls import path
from .views
from .views import list_books, LibraryDetailView

urlpatterns = [
    path("books/", list_books, name="book_list"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('admin/', views.admin_view, name='admin_view'),

]
