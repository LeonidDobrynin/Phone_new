from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sorting = request.GET["sort"]
    template = 'catalog.html'
    if sorting != None:
        if sorting == 'name':
            phones = Phone.objects.order_by('name')
            print(phones)
            context = {'phones': phones}

        if sorting == 'min_price':
            phones = Phone.objects.order_by('price')
            print(phones)
            context = {'phones': phones}

        if sorting == 'max_price':
            phones = Phone.objects.order_by('-price')
            print(phones)
            context = {'phones': phones}


    else:
        phones = Phone.objects.all()
        print(phones)
        context = {'phones':phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phones = Phone.objects.filter(slug=slug)
    for phone in phones:
        print(phone)
    context = {'phone':phone}
    return render(request, template, context)
