from django.urls import include, path
from . import views

urlpatterns = [
    path('contact', views.ContactView.as_view(), name='contact'),  # contact
    path('account', views.AccountView.as_view(), name='account'),  # account
    path('account/detail', views.AccountDetailView.as_view(), name='account'),  # account detail
]