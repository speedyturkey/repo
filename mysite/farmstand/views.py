from django.shortcuts import render
from settings import *


def home(request):

    context_dict = []

    return render(request, 'farmstand/home.html', context_dict)
    
def products(request):

    context_dict = []

    return render(request, 'farmstand/products.html', context_dict)