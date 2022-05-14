from django.shortcuts import render
from django.views import View
from .forms import *
from django.contrib import messages
from django.views.generic import UpdateView, CreateView
from django.urls import reverse_lazy


# Dashboard
class DashboardView(View):
    def get(self, request):
        print("dashboard called")
        greeting = {}
        greeting['title'] = "Dashboard"
        greeting['pageview'] = "TOI"
        return render(request, 'menu/index.html', greeting)


# create product
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
class ProductListView(View):
    def get(self, request):
        context = {
            'product': Product.objects.all(),
            'title': "Product List",
            'pageview': "Product"
        }
        return render(request, 'menu/product-list.html', context)