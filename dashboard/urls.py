from django.urls import include, path
from . import views

urlpatterns = [
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),  # dashboard
    path('dashboard/product-create', views.create_product, name='product-create'),  # Product create
    path('dashboard/product-list', views.ProductListView.as_view(), name='dash-product'),  # Product list
    path('dashboard/product-edit/<int:pk>', views.ProductUpdateView.as_view(), name='product-edit'),  # Product edit
    path('delete-product/<int:pk>', views.product_delete, name='delete-product'),  # Product delete

]