from django.shortcuts import render
from .models import Product

# Create your views here.
def product_page(request):
    products = Product.objects.all()
    context = {
        "all_products": products
    }
    return render(request, "product.html", context)


def about(request):
    return render(request, "about.html")