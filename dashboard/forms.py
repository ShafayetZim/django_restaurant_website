from django import forms
from .models import Product, OrderUpdate


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'product_name', 'category', 'price', 'desc', 'pub_date', 'image',)
        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'desc': forms.TextInput(attrs={'class': 'form-control'}),
            'pub_date': forms.DateInput(attrs={'type': 'date'}),
            'image': forms.FileInput(attrs={'class': 'rounded_list'}),

        }


class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'product_name', 'category', 'price', 'desc', 'pub_date', 'image',)
        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'desc': forms.TextInput(attrs={'class': 'form-control'}),
            'pub_date': forms.DateInput(attrs={'type': 'date'}),
            'image': forms.FileInput(attrs={'class': 'rounded_list'}),

        }


class TrackingForm(forms.ModelForm):
    class Meta:
        model = OrderUpdate
        fields = (
            'order_id', 'update_desc')
        widgets = {
            'order_id': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'update_desc': forms.TextInput(attrs={'class': 'form-control'}),

        }
