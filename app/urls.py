from django.urls import path
from .views import login, home, carrito, pago

urlpatterns = [
    path('', login,name='login'),
    path('home/', home,name='home'),
    path('carrito/', carrito,name='carrito'),
    path('pago/', pago,name='pago'),
]