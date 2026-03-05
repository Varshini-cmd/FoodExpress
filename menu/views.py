from django.shortcuts import render
from.models import FoodItem
def home(request):
    items = FoodItem.objects.all()
    return render(request, 'menu/home.html', {'items': items})