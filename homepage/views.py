from bombocados_restaurant.settings import BASE_DIR

# Create your views here.
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')
