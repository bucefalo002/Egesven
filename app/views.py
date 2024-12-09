from django.shortcuts import render, redirect,get_object_or_404
from .models import Producto
from .forms import ProductoForm

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

def agregar(request):
    data = {
        'form':ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Guardado correctamente'
        else:
            data['form'] = formulario
    return render(request,'app/productos/agregar.html',data)

def listar(request):
    productos=Producto.objects.all()
    data={
        'productos':productos
    }
    return render(request, 'app/productos/listar.html',data)


def editar(request,id):
    producto = get_object_or_404(Producto, id=id)
    data={
        'form':ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='listar')
        data['form'] = formulario
        
    return render(request,'app/productos/editar.html',data)

def eliminar(request,id):
    producto = get_object_or_404(Producto,id=id)
    producto.delete()
    return redirect(to="listar")
