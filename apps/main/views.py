from django.shortcuts import render


def main(request):
    return render(request, 'main/main.html', {'title': 'Семена деревьев'})


def contact(request):
    return render(request, 'main/contact.html', {'title': 'Контакты'})
