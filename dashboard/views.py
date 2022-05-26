from django.shortcuts import render, redirect
from django.views import View
from .models import *
from .forms import *
from django.contrib import messages
from django.views.generic import UpdateView, CreateView, ListView
from django.urls import reverse_lazy

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Dashboard
class DashboardView(LoginRequiredMixin,View):
    login_url = 'admin-login'
    def get(self, request):
        print("dashboard called")
        greeting = {}
        greeting['title'] = "Dashboard"
        greeting['pageview'] = "TOI"
        return render(request, 'menu/index.html', greeting)


# create product
@login_required(login_url='admin-login')
def create_product(request):
   if request.method == "POST":
    form = ProductCreateForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      img_obj = form.instance
      return render(request, 'menu/create-product.html', {'form': form, 'img_obj': img_obj})

   else:
      form = ProductCreateForm()
   return render(request, 'menu/create-product.html', {'form': form, 'title': "Create Product", 'pageview': "Product"})


# product list
class ProductListView(LoginRequiredMixin, View):
    login_url = 'admin-login'
    def get(self, request):
        context = {
            'product': Product.objects.all(),
            'title': "Product List",
            'pageview': "Product"
        }
        return render(request, 'menu/product-list.html', context)


# edit-product
class ProductUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'admin-login'
    model = Product
    form_class = ProductUpdateForm
    success_url = reverse_lazy('dash-product')
    template_name = 'menu/edit-product.html'

    success_message = "Product was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context["title"] = "Update Product"
        context["pageview"] = "Product"
        return context


# product-delete
@login_required(login_url='admin-login')
def product_delete(request, id):
    if request.method == 'GET':
        instance = Product.objects.get(id=id)
        instance.delete()
        messages.add_message(request, messages.WARNING, 'Delete Success')
        return redirect('dash-product')


# order list view
class OrderListView(LoginRequiredMixin, ListView, ):
    login_url = 'admin-login'
    model = Orders  # Model I want to Covert to List
    template_name = 'menu/order-table.html'  # Template Name
    context_object_name = 'order'  # Change default name of objectList
    ordering = ['-timestamp', '-order_id']  # Ordering post LIFO

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Order Table"
        context["pageview"] = "Order"
        return context


# tracking list view
class TrackingListView(LoginRequiredMixin, ListView, ):
    login_url = 'admin-login'
    model = OrderUpdate  # Model I want to Covert to List
    template_name = 'menu/order-tracking.html'  # Template Name
    context_object_name = 'tracking'  # Change default name of objectList
    ordering = ['-timestamp', '-order_id']  # Ordering post LIFO

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Order Tracking"
        context["pageview"] = "Order"
        return context


class TrackingChangeView(LoginRequiredMixin, UpdateView):
    login_url = 'admin-login'
    model = OrderUpdate
    form_class = TrackingForm
    success_url = reverse_lazy('order-tracking')
    template_name = 'menu/change-tracking.html'

    success_message = "Order Tracking was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context["title"] = "Change Tracking"
        context["pageview"] = "Tracking List"
        return context


# admin login
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Username OR Password is incorrect')

    context = {}
    return render(request, 'accounts/login.html', context)


# admin logout
def logoutAdmin(request):
    logout(request)
    return redirect('admin-login')
