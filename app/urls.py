from django.urls import path
from .views import login, home, carrito, pago,agregar,listar,editar,eliminar

urlpatterns = [
    path('', login,name='login'),
    path('home/', home,name='home'),
    path('carrito/', carrito,name='carrito'),
    path('pago/', pago,name='pago'),
    path('agregar/',agregar,name='agregar'),
    path('listar/',listar,name='listar'),
    path('editar/<id>/',editar,name='editar'),
    path('eliminar/<id>/',eliminar,name='eliminar'),
]