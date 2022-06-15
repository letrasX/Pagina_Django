from django.shortcuts import render, redirect
from .forms import VehiculoForm
from .models import Vehiculo

# Create your views here.
def home(request):
    #accedendo al objeto que contiene los datos de la base
    #el metodo all traera todos los vehiculos que estan en la tabla
    vehiculos= Vehiculo.objects.all()
    #ahora crearemos una variable que le pase los datos del vehiculo al template
    datos = {
        'vehiculos':vehiculos
    }
    #ahora lo agregamos para que se envie al template
    return render(request, 'core/home.html', datos)

def form_vehiculo(request):
    datos ={
        'form': VehiculoForm()
    }
    #verificamos que peticion sean post y rescatamos los datos
    if request.method== 'POST':
        #CONREQUEST RECUPERAMOS LOS DATOS DEL FORMULARIO
        formulario = VehiculoForm(request.POST)
        #Y VALIDAMOS EL FORMULARIO
        if formulario.is_valid:
            #ahoraguardamos en la base de datos
            formulario.save()
            #y mostramos un mensaje
            datos['mensaje'] = "Guardados correctamente"
    return render(request, 'core/form_vehiculo.html',datos) 
def form_mod_vehiculo(request,id):
    #el id es el identificador del vehiculo
    # buscando los datos en la tabla
    # buscamos por patente que llega como dato en la url
        vehiculo = Vehiculo.objects.get(patente=id)
        #ahora le entregamos los datos del vehiculo al formulario
        datos={
            'form': VehiculoForm(instance=vehiculo)
        }  
        #verificamos que peticion sean post y rescatamos los datos
        if request.method== 'POST':
        #CONREQUEST RECUPERAMOS LOS DATOS DEL FORMULARIO
            formulario = VehiculoForm(data=request.POST, instance=vehiculo)
        #Y VALIDAMOS EL FORMULARIO
            if formulario.is_valid:
            #ahoraguardamos en la base de datos
                formulario.save()
            #y mostramos un mensaje
                datos['mensaje'] = "los datos se han modificado correctamente"
        return render(request, 'core/form_mod_vehiculo.html',datos)   

def form_del_vehiculo(request, id):
    #el id es el identificador de la tabla de vehiculos
    #buscando los datos en la base de datos
    vehiculo = Vehiculo.objects.get(patente=id)
    #eliminamos el vehiculo de la patente buscada
    vehiculo.delete()
    #y ahora redirifimos a la pagina homme con el listado
    return redirect(to="home")