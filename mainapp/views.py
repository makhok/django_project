import json
import os.path

from django.shortcuts import render

# Create your views here.

main_menu = [
    {'href': 'index', 'name': 'домой'},
    {'href': 'products', 'name': 'продукты'},
    {'href': 'contact', 'name': 'контакты'},
]

module_dir = os.path.dirname(__file__)

def index(request):
    content = {
        'title': 'магазин',
        'main_menu': main_menu,
    }
    return render(request, 'mainapp/index.html', content)

def products(request):
    file_path = os.path.join(module_dir, 'fixtures/products.json')
    products = json.load(open(file_path, encoding='utf-8'))
    content = {
        'title': 'каталог',
        'main_menu': main_menu,
        'products': products,
    }
    return render(request, 'mainapp/products.html', content)

def contact(request):
    content = {
        'title': 'контакты',
        'main_menu': main_menu,
    }
    return render(request, 'mainapp/contact.html', content)
