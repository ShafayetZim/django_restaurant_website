from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),  # home
    path('about', views.AboutView.as_view(), name='about'),  # about
    path('menu', views.MenuView.as_view(), name='menu'),  # menu
    path('shop_cart', views.ShopCartView.as_view(), name='shop-cart'),  # shop-cart
    path('shop_checkout', views.ShopCheckoutView.as_view(), name='shop-checkout'),  # shop-checkout
    path('signup/', views.handleSignUp, name='handleSignUp'),
    path('login/', views.handeLogin, name="handleLogin"),
    path('logout/', views.handleLogout, name="handleLogout"),
    path('checkout/', views.checkout, name="Checkout"),
    path('orderView', views.orderView, name="orderView"),
    path('tracker', views.tracker, name="TrackingStatus"),
]
