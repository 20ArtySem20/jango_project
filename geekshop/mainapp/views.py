from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def products(request):
    return render(request, "products.html")
