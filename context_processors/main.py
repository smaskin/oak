def header(request):
    return {
        'site_name': 'Семена деревьев',
        'menu': [
            {'href': 'main', 'name': 'Главная'},
            {'href': 'products:index', 'name': 'Каталог'},
            {'href': 'contact', 'name': 'Контакты'},
        ]
    }
