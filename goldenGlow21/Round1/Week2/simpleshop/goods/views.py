from django.shortcuts import render
from .models import Product


# Create your views here.
def index(request):
    goods = Product.objects.all()
    return render(request, 'goods/index.html', {'goods': goods})

