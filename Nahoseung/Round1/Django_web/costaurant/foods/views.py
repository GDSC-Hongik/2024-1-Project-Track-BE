from django.shortcuts import render
from django.http import HttpResponse,Http404
from datetime import datetime
from foods.models import menu

def index(request):
    context=dict()
    today=datetime.today().date()
    menus=menu.objects.all()
    context["date"]=today
    context["menus"]=menus
    return render(request,'foods/index.html',context=context)

def food_detail(request,pk):
    context=dict()
    menus=menu.objects.get(id=pk)
    context["menu"]=menus
    
    return render(request,'foods/detail.html',context)

#HttpResponse("<h2> Hello World\n this is BC<h2>")
