from django.shortcuts import render, redirect,get_object_or_404
from .models import Producto, Usuario
from .forms import ProductoForm,LoginForm
from django.contrib import messages

# Create your views here.


def login(request):
    data = {
        'form': LoginForm()
    }
    if request.method == 'POST':
        nombre = request.POST.get('username')
        usuario = Usuario.objects.filter(nombre=nombre).first()

        if usuario:
            # Guardar los datos del usuario en la sesión
            request.session['usuario_nombre'] = usuario.nombre
            request.session['usuario_rol'] = usuario.rol
            return redirect(to='home')
        else:
            data['error'] = 'Usuario no encontrado'

    return render(request, 'app/login.html', data)

def home(request):
    usuario_nombre = request.session.get('usuario_nombre')
    usuario_rol = request.session.get('usuario_rol')

    productos = Producto.objects.all()
    data = {
        'productos': productos,
        'usuario_nombre': usuario_nombre,
        'usuario_rol': usuario_rol,
    }
    return render(request, 'app/home.html', data)

def carrito(request):
    return render(request, 'app/carrito.html')

def pago(request):
    return render(request, 'app/pago.html')

def agregar(request):
    usuario_nombre = request.session.get('usuario_nombre')
    usuario_rol = request.session.get('usuario_rol')
    data = {
        'form':ProductoForm(),
        'usuario_nombre': usuario_nombre,
        'usuario_rol': usuario_rol,
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
    usuario_nombre = request.session.get('usuario_nombre')
    usuario_rol = request.session.get('usuario_rol')
    productos=Producto.objects.all()
    data={
        'productos':productos,
        'usuario_nombre': usuario_nombre,
        'usuario_rol': usuario_rol,
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
            messages.success(request,'Modificado correctamente')
            return redirect(to='listar')
        data['form'] = formulario
        
    return render(request,'app/productos/editar.html',data)

def eliminar(request,id):
    producto = get_object_or_404(Producto,id=id)
    producto.delete()
    messages.success(request,'Eliminado correctamente')
    return redirect(to="listar")
