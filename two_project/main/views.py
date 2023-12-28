from django.shortcuts import render


def index(request):

    data = {
        'title': 'Главная страница!',
        'about': 'О нас'
    }
    return render(request,'main/index.html', data)

def about(request):
    data = {
        'title': 'Главная страница!',
        'about': 'О нас',
        'news': 'Новости!'
    }
    return render(request, 'main/about.html', data)
