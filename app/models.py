from django.db import models

# Create your models here.
class Usuario(models.Model):
    ROLES=(
        (1,"administrador"),
        (2,"usuario")
    )
    idUsuario=models.BigAutoField(primary_key=True, blank=True)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    contacto=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    nombreUsuario=models.CharField(max_length=50)
    contrasena=models.CharField(max_length=50)
    rol=models.IntegerField(choices=ROLES,default=2)
    def __str__(self):
        return f"{self.nombre}"

class MaquinaDeCoser(models.Model):
    id=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=150)
    rpm=models.IntegerField()
    puntadas_por_min=models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre}"
    
class operacion(models.Model):
    codigo=models.CharField(primary_key=True,blank=True,max_length=150)
    nombre=models.CharField(max_length=150)
    def __str__(self):
        return f"{self.nombre}"
    
class Suplemento(models.Model):
    id=models.BigAutoField(primary_key=True,blank=True)
    porcentaje=models.CharField(max_length=150,null=True)
    def __str__(self):
        return f"{self.porcentaje}"

class Turno(models.Model):
    id=models.BigAutoField(primary_key=True,blank=True)
    turno=models.IntegerField(null=True)
    def __str__(self):
        return f"{self.turno}"
    
class Gtf(models.Model):
    idGtf=models.BigAutoField(primary_key=True,blank=True)
    referencia=models.CharField(max_length=150)
    valor=models.FloatField(default=0.0)
    def __str__(self):
        return f"{self.valor}"
    

class Presicion_de_parada(models.Model):
    idParada=models.BigAutoField(primary_key=True,blank=True)
    referencia=models.CharField(max_length=150)
    valor=models.FloatField(default=0.0)
    def __str__(self):
        return f"{self.valor}"


    
class FichaTecnica(models.Model):
    idFicha=models.BigAutoField(primary_key=True, blank=True)
    idUsuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    fecha=models.DateField()
    operacion=models.ForeignKey(operacion,on_delete=models.CASCADE)
    codigo_Operacion=models.CharField(max_length=150)
    tipoMaquina=models.ForeignKey(MaquinaDeCoser,on_delete=models.CASCADE)
    ref=models.CharField(max_length=150)
    rpm=models.IntegerField()
    modulo=models.CharField(max_length=150)
    ppp=models.CharField(max_length=150)
    minTurno=models.ForeignKey(Turno,on_delete=models.CASCADE)
    suplementos=models.ForeignKey(Suplemento,on_delete=models.CASCADE)
    tipoTela=models.CharField(max_length=150)
    tiempoMinimoCostura=models.FloatField(default=0.0)
    gtf=models.ForeignKey(Gtf,on_delete=models.CASCADE)
    distanciaCostura=models.FloatField(default=0.0)
    numeroParadas=models.IntegerField(default=0)
    constante=models.FloatField(default=0.0006)
    factorAltaVelocidad=models.FloatField(default=0.0)
    paradaArranque=models.IntegerField(default=0)
    presicionParada=models.ForeignKey(Presicion_de_parada,on_delete=models.CASCADE)
    tmuCostura=models.FloatField(default=0.0)
    def __str__(self):
        return f"{self.idFicha}-{self.operacion}"


class Codigos_GSD(models.Model):
    Numero=models.IntegerField(primary_key=True,blank=True)
    codigo=models.CharField(max_length=150)
    movimiento=models.CharField(max_length=150)
    tmu=models.IntegerField()
    dn=models.IntegerField(blank=True,null=True)
    secuencia=models.CharField(max_length=150, blank=True,null=True)
    v1=models.FloatField(blank=True,null=True)
    v2=models.FloatField(blank=True,null=True)
    v3=models.FloatField(blank=True,null=True)
    v4=models.FloatField(blank=True,null=True)
    v5=models.FloatField(blank=True,null=True)


class FormularioDinamico(models.Model):
    id=models.BigAutoField(primary_key=True, blank=True)
    fichaTecnica=models.ForeignKey(FichaTecnica,on_delete=models.CASCADE)
    Numero=models.IntegerField()
    codigo=models.CharField(max_length=150)
    movimiento=models.CharField(max_length=150)
    frecuencia=models.IntegerField()
    distancia=models.IntegerField()
    tmu=models.IntegerField()
    totalTmu=models.FloatField()
    tiempoSam=models.FloatField()
    
