from django.urls import path
from .views import login, home, carrito, pago,agregar

urlpatterns = [
    path('', login,name='login'),
    path('home/', home,name='home'),
    path('carrito/', carrito,name='carrito'),
    path('pago/', pago,name='pago'),
    path('agregar/',agregar,name='agregar'),
]