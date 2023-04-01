from django.urls import path
from . import views
from .views import PostlistView,PostDetailView

urlpatterns = [
    # path('', views.home, name='blog-home'),
    path('',PostlistView.as_view(), name='blog-home'),
    path('post/<int:pk>/',PostDetailView.as_view(), name='blog-home'),
    path('about/', views.about, name = 'blog-about')
    ]