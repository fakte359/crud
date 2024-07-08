from django.db import models

class Productos(models.Model):
    nombre=models.CharField(max_length=255)
    proveedor=models.CharField(max_length=255)
    id_producto=models.CharField(max_length=255, unique=True)
    precio=models.DecimalField( max_digits=10, decimal_places=3)
    
   
    

# Create your models here.