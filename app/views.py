from django.shortcuts import render
from .models import *
# Create your views here.

def listar_fichat(request):
    q=FichaTecnica.objects.all()
    contex={"data":q}
    return render(request,'app/ficha/listar_fichat.html',contex)

def form_fichat(request):
    U=Usuario.objects.all()
    O=operacion.objects.all()
    M=MaquinaDeCoser.objects.all()
    T=Turno.objects.all()
    S=Suplemento.objects.all()
    contex={"usuarios":U,"operaciones":O,"maquinas":M,"turnos":T,"suplementos":S}
    return render(request,'app/ficha/form_listar.html',contex)