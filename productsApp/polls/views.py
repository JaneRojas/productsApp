from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def createProduct(request, product_id):
    return HttpResponse("You're creating a product %s." % product_id)

