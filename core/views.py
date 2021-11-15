from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.shortcuts import render

from core.models import Product


def home(request, c_slug=None):
    products_list = Product.objects.all()
    paginator = Paginator(products_list, 200)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)
    return render(request, 'home.html', {'products': products})


def ProdDetail(request, pk):
    try:
        product = Product.objects.get(id=pk)
    except Exception as e:
        raise e
    return render(request, 'product.html', {'product': product})
