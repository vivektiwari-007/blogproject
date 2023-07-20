from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Other URL patterns
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.home, name='home'),
    path('create/', views.post_create, name='post-create'),
    path('update/<int:pk>/', views.post_update, name='post-update'),
    path('delete/<int:pk>/', views.post_delete, name='post-delete'),
    # Add other URL patterns for details, create, update, delete, etc.
]
