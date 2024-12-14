from django import forms
from .models import Producto,Usuario

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'

class LoginForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = '__all__'