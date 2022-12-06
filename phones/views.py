from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phone = Phone.objects.all()
    context = {'phone':phone}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.object.filter(slug=slug)
    context = {'phone':phone}
    return render(request, template, context)
