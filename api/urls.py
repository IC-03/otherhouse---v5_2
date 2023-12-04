from django.urls import path,include
from rest_framework import routers
from api import views


router = routers.DefaultRouter()
router.register(r'usuarios',views.UsuarioViewset)
router.register(r'inmuebles', views.InmuebleViewSet)
router.register(r'arriendos', views.ArriendoViewSet)
router.register(r'ServiciosAdicionales', views.ServicioAdicionalViewSet)
router.register(r'direcciones', views.DireccionViewSet)
urlpatterns = [
    path('', include(router.urls)),
]

