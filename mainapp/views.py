import json
import os.path

from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Create your views here.
from basketapp.models import Basket
from mainapp.models import Product, ProductCategory

menu = [
    {'href': 'main', 'name': 'домой'},
    {'href': 'products:index', 'name': 'продукты'},
    {'href': 'contact', 'name': 'контакты'},
]

module_dir = os.path.dirname(__file__)


def index(request):
    content = {
        'title': 'магазин',
        'menu': menu,
    }
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    print(pk)

    title = 'продукты'
    links_menu = ProductCategory.objects.all()

    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        content = {
            'title': title,
            'links_menu': links_menu,
            'products': products,
            'category': category,
            'menu': menu,
            'basket': basket,
        }

        return render(request, 'mainapp/products_list.html', content)

    same_products = Product.objects.all()[:5]

    content = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products,
        'menu': menu
    }

    return render(request, 'mainapp/products.html', content)


def contact(request):
    content = {
        'title': 'контакты',
        'menu': menu,
    }
    return render(request, 'mainapp/contact.html', content)


def main(request):
    title = 'главная'
    products = Product.objects.all()[:3]
    content = {'title': title, 'products': products, 'menu': menu}
    return render(request, 'mainapp/index.html', content)


