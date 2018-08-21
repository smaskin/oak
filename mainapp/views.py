from django.shortcuts import render


def get_content():
    title ='Семена деревьев'
    menu = [
        {'href': 'main', 'name': 'Главная'},
        {'href': 'products', 'name': 'Каталог'},
        {'href': 'contact', 'name': 'Контакты'},
    ]
    return {
        'title': title,
        'menu': menu,
    }


def main(request):
    return render(request, 'mainapp/index.html', get_content())


def products(request):
    products = [
        {'href': 'detail', 'name': 'Дуб', 'img': 'images/oak.jpeg'},
        {'href': 'detail', 'name': 'Липа', 'img': 'images/linden.jpeg'},
        {'href': 'detail', 'name': 'Клен', 'img': 'images/maple.jpeg'},
    ]
    content = get_content()
    content['products'] = products
    return render(request, 'mainapp/products.html', content)


def contact(request):
    return render(request, 'mainapp/contact.html', get_content())


def detail(request):
    return render(request, 'mainapp/detail.html', get_content())
