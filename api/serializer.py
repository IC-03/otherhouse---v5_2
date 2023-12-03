from rest_framework import serializers
from .models import Usuario
from .models import Inmueble
from .models import Arriendo
from .models import ServicioAdicional
from .models import Direccion

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields ='__all__'

class InmuebleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inmueble
        fields ='__all__'

class ArriendoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arriendo
        fields ='__all__'

class ServicioAdicionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicioAdicional
        fields ='__all__'

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields ='__all__'