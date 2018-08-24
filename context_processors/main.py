def menu(request):
    return {
        'menu': [
            {'href': 'main', 'name': 'Главная'},
            {'href': 'products:index', 'name': 'Каталог'},
            {'href': 'contact', 'name': 'Контакты'},
        ]
    }
