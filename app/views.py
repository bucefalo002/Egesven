from django.shortcuts import render, redirect
from .models import Producto

# Create your views here.


def login(request):
    return render(request, 'app/login.html')

def home(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/home.html', data)

def carrito(request):
    return render(request, 'app/carrito.html')

def pago(request):
    return render(request, 'app/pago.html')


