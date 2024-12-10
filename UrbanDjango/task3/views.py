from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'third_task/index.html')


def shop(request):
    items = {
        'Игровая приставка': '30000 руб.',
        'Игра "Приключения"': '2500 руб.',
        'Контроллер': '1500 руб.'
    }
    return render(request, 'third_task/shop.html', {'items': items})


def cart(request):
    return render(request, 'third_task/cart.html')