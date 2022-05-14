from django.urls import include, path
from . import views

urlpatterns = [
    path('blog', views.BlogView.as_view(), name='blog'),  # blog
    path('blog/detail', views.BlogDetailView.as_view(), name='blog-detail'),  # blog detail
    path('gallery', views.GalleryView.as_view(), name='gallery'),  # gallery
]