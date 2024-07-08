from django import forms

from .models import Productos


class ProductosForm(forms.ModelForm):
    
    class Meta:
        model = Productos
        fields = ['nombre','proveedor','id_producto', 'precio']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese producto'}),
            'proveedor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese proveedor'}),
            'id_producto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Id producto'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese precio'}),
        }
        




