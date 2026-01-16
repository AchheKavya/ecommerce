from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Category, Product

def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'store/home.html', {
        'categories': categories,
        'products': products
    })
