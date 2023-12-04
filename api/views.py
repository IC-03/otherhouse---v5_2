from rest_framework import viewsets
from .serializer import UsuarioSerializer
from .serializer import InmuebleSerializer
from .serializer import ArriendoSerializer
from .serializer import ServicioAdicionalSerializer
from .serializer import DireccionSerializer
from .models import Direccion
from .models import Usuario
from .models import Inmueble
from .models import Arriendo
from .models import ServicioAdicional





class UsuarioViewset(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class= UsuarioSerializer

class InmuebleViewSet(viewsets.ModelViewSet):
    queryset = Inmueble.objects.all()
    serializer_class = InmuebleSerializer

class ArriendoViewSet(viewsets.ModelViewSet):
    queryset = Arriendo.objects.all()
    serializer_class = ArriendoSerializer

class ServicioAdicionalViewSet(viewsets.ModelViewSet):
    queryset = ServicioAdicional.objects.all()
    serializer_class = ServicioAdicionalSerializer

class DireccionViewSet(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer
