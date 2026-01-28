from django.shortcuts import render

from base.models import Product


def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'base/main.html', context)