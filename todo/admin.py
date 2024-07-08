from django.contrib import admin
from .models import Productos

@admin.register(Productos)
class Productosadmin(admin.ModelAdmin):
    list_display = ('nombre', 'proveedor', 'id_producto', 'precio')

# Register your models here.
