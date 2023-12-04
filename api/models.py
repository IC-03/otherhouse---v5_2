from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=100)
    tel = models.IntegerField()
    fecha_nac = models.DateField()
    tipo_doc = models.TextField()
    num_doc = models.IntegerField()
    correo = models.CharField(max_length=100)

class Direccion(models.Model):
    direccion = models.CharField(max_length=100)
    pais = models.CharField(max_length=100, default='Colombia')
    ciudad = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    barrio = models.CharField(max_length=100, blank=True, null=True)
    detalles_adicionales = models.TextField(blank=True, null=True)
    

class Inmueble(models.Model):
    arrendador = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=1)
    descripcion = models.TextField()    
    tamano = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    preciobase =  models.IntegerField()
    cupo = models.IntegerField()
    servicios_base = models.TextField()
    servicios_ad = models.TextField()
    num_banos = models.IntegerField()
    petfriendly = models.BooleanField()
    def __str__(self):
        return f'{self.descripcion} - {self.arrendador.username}' if self.arrendador else 'Inmueble sin arrendador'
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.descripcion} - {self.arrendador.username}' if self.arrendador else 'Inmueble sin arrendador'


class Arriendo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    def __str__(self):
        return f'{self.usuario.username}'
    def calcular_total_a_pagar(self):
        total_a_pagar = self.inmueble.preciobase
        servicios_adicionales = ServicioAdicional.objects.filter(inmueble=self.inmueble)
        if servicios_adicionales.exists():
            total_a_pagar += sum(servicio.precio for servicio in servicios_adicionales)
        return total_a_pagar
   

class ServicioAdicional(models.Model):
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE, default=1)
    servicio = models.CharField(max_length=100)
    precio = models.IntegerField()

