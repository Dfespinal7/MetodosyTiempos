from django.shortcuts import render
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages 
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
    G=Gtf.objects.all()
    P=Presicion_de_parada.objects.all()
    contex={"usuarios":U,"operaciones":O,"maquinas":M,"turnos":T,"suplementos":S,"gtfs":G,"paradas":P}
    return render(request,'app/ficha/form_listar.html',contex)


def guardar_ficha_tecnica(request):
    if request.method=='POST':
        
        usuario=Usuario.objects.get(pk=request.POST.get("usuario"))
        fecha=request.POST.get("fecha")
        opera=operacion.objects.get(pk=request.POST.get("operacion"))
        cod_operacion=request.POST.get("cod_operacion")
        tipo_maquina=MaquinaDeCoser.objects.get(pk=request.POST.get("tipo_maquina"))
        ref=request.POST.get("ref")
        rpm=request.POST.get("rpm")
        modulo=request.POST.get("modulo")
        ppp=request.POST.get("ppp")
        min_turno=Turno.objects.get(pk=request.POST.get("min_turno"))
        suplementos=Suplemento.objects.get(pk=request.POST.get("suplementos"))
        tela=request.POST.get("tela")
        mts=request.POST.get("mts")
        gtf=Gtf.objects.get(pk=request.POST.get("gtf"))
        los=request.POST.get("los")
        nparadas=request.POST.get("nparadas")
        consta=request.POST.get("consta")
        hsf=request.POST.get("hsf")
        ss=request.POST.get("ss")
        parad=Presicion_de_parada.objects.get(pk=request.POST.get("parad"))
        tmu=request.POST.get("tmu")
        try:
            ficha=FichaTecnica(idUsuario=usuario,fecha=fecha,operacion=opera,codigo_Operacion=cod_operacion,tipoMaquina=tipo_maquina,ref=ref,rpm=rpm,modulo=modulo,minTurno=min_turno,ppp=ppp,suplementos=suplementos,tipoTela=tela,tiempoMinimoCostura=mts,gtf=gtf,distanciaCostura=los,numeroParadas=nparadas,constante=consta,factorAltaVelocidad=hsf,paradaArranque=ss,presicionParada=parad,tmuCostura=tmu)
            ficha.save()
            messages.success(request,"ficha creada correctamente")
        except Exception as e:
            messages.warning(request, f"error.{e}")
        return HttpResponseRedirect(reverse("listar_ficha"))
            






