from django.shortcuts import render
from django.views import View


# contact
class ContactView(View):
    def get(self, request):
        print("contact called")

        return render(request, 'web/contact.html')


# shop account
class AccountView(View):
    def get(self, request):
        print("account called")

        return render(request, 'web/shop_account.html')


# shop account detail
class AccountDetailView(View):
    def get(self, request):
        print("account detail called")

        return render(request, 'web/shop_account_detail.html')
