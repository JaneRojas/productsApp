from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Product

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def createProduct(request, product_id):
    return HttpResponse("You're creating a product %s." % product_id)

def productLastExample(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/createProduct.html', {'product': product})

def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'polls/createProduct.html', {'product': product})