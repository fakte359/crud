from django.shortcuts import render, redirect

from .forms import ProductosForm

from .models import Productos

def home(request):
    producto=Productos.objects.all()
    context={'producto':producto}
    return render(request,'todo/home.html',context)

def agregar(request):
    if request.method =="POST":
        form =ProductosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductosForm()
        
    context = {'form': form}
    return render(request, 'todo/agregar.html', context)

def eliminar(request,p_id):
    producto=Productos.objects.get(id=p_id)
    producto.delete()
    return redirect("home")

def editar(request, p_id):
    producto=Productos.objects.get(id=p_id)
    if request.method=="POST":
        form=ProductosForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect("home")
        
    else:
        form=ProductosForm(instance=producto)
    context={"form":form}
    return render(request,"todo/editar.html", context)
        

        


        
    



# Create your views here.
