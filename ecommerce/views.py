from django.shortcuts import render
from .models import Product, Latest_Post

# Create your views here.
def product_page(request):
    products = Product.objects.all()
    context = {
        "all_products": products
    }
    return render(request, "product.html", context)


def about(request):
    return render(request, "about.html")

def single_product_view(request, id):
    product = Product.objects.get(id=id)
    context = {
        "product": product
    }
    return render(request, "products_details.html", context)

def latest_post(request):
    latest = Latest_Post.objects.all()
    context = {
        "all_latest_post": latest
    }
    return render(request, "latest_post.html", context)

def single_latest_post(request, pk):
    latest1 = Latest_Post.objects.get(pk=pk)
    context = {
        "specific_latest_post": latest1
    }
    return render(request, "latest_details.html", context)

def announcement_page(request):
    return render(request, "announcement.html")

def calendar_page(request):
    return render(request, "calendar.html")

