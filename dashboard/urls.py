from django.urls import include, path
from . import views

urlpatterns = [
    path('dashboard', views.DashboardView.as_view(), name='dashboard'),  # dashboard
    path('dashboard/product-create', views.create_product, name='product-create'),  # Product create
    path('dashboard/product-list', views.ProductListView.as_view(), name='dash-product'),  # Product list

]