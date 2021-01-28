from django.shortcuts import render
from mainapp.models import Products, ProductCategory


def index(request):
    context = {'title': 'Soul Shop'}
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'Soul Products',
        'products': Products.objects.all(),
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'mainapp/products.html', context)

