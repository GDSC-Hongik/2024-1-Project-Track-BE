from django.shortcuts import render
from datetime import datetime
from .models import Menu


# Create your views here.
def index(request):
    context = dict()
    today = str(datetime.today().date())
    menus = Menu.objects.all()
    context['date'] = today
    context['menus'] = menus
    return render(request, 'foods/index.html', context)


def food_detail(request, pk):
    menu = Menu.objects.get(id=pk)
    context = {'menu': menu}
    return render(request, 'foods/detail.html', context)
