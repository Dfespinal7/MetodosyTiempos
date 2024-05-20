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

class FichaTecnica(models.Model):
    idFicha=models.BigAutoField(primary_key=True, blank=True)
    idUsuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    fecha=models.DateField()
    operacion=models.CharField(max_length=150)
    codigo_Operacion=models.CharField(max_length=150)
    tipoMaquina=models.ForeignKey(MaquinaDeCoser,on_delete=models.CASCADE)
    ref=models.CharField(max_length=150)
    rpm=models.IntegerField()
    modulo=models.CharField(max_length=150)
    ppp=models.CharField(max_length=150)
    minTurno=models.IntegerField()
    suplementos=models.CharField(max_length=150)


