from django.contrib import admin
from .models import Usuario, Producto

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre','precio','stock']
    list_editable = ['precio']
    search_fields = ['nombre']

admin.site.register(Usuario)
admin.site.register(Producto)