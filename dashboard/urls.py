from django.urls import include, path
from . import views

urlpatterns = [
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),  # dashboard
    path('dashboard/product-create', views.create_product, name='product-create'),  # Product create
    path('dashboard/product-list', views.ProductListView.as_view(), name='dash-product'),  # Product list
    path('dashboard/product-edit/<int:pk>', views.ProductUpdateView.as_view(), name='product-edit'),  # Product edit
    path('delete-product/<int:id>', views.product_delete, name='delete-product'),  # Product delete
    path('order-table', views.OrderListView.as_view(), name="order-table"),  # order list
    path('order-tracking', views.TrackingListView.as_view(), name="order-tracking"),  # tracking list
    path('change-tracking/<int:pk>', views.TrackingChangeView.as_view(), name='change-tracking'),  # track-parcel

]