from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product


def say_hello(request):
    Product.objects.all()

    return render(request, 'hello.html', { 'name':'abdelhalim'})
