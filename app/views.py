from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request, 'app/login.html')

def home(request):
    return render(request, 'app/home.html')

def carrito(request):
    return render(request, 'app/carrito.html')

def pago(request):
    return render(request, 'app/pago.html')
