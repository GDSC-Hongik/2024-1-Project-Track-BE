from django.shortcuts import render
from django.http import HttpResponse 
from datetime import datetime
from django.http import Http404
from foods.models import Menu

# Create your views here.
def index(request):

    context  = dict()
    today = datetime.today().date()
    context["date"] = today
    menus = Menu.objects.all()
    context["menus"] = menus
    return render(request,'foods/index.html',context=context)


def chicken(request):
    return render(request, 'foods/chicken.html')

def food_detail(request,pk):
    context = dict()
    menu = Menu.object.get(id=pk)
    context["menu"] = menu
    return render(request,'foods/detail.html',context=context)