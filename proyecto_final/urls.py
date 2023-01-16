from urllib import request

from django.test import TestCase
from django.contrib.auth import views as auth_views

# Create your tests here.
from django.urls import path, include
from . import views
from .views import Home, ArtistaListView, ObraListView, Registrar, ArtistCreate, \
    ObraCreate, UpdateArtista, UpdateObra, EliminarArtista, EliminarObra

urlpatterns = [
    path('', Home.as_view(), name='index'),
    path('accounts/logout', auth_views.LogoutView.as_view(template_name='accounts/login'), name='logout'),
    path('artista', ArtistaListView.as_view(), name='artista'),
    path('obra', ObraListView.as_view(), name='obra'),
    # path('modalidad', Modality.as_view(), name='modalidad'),
    # path('eventos', Eventos.as_view(), name='eventos'),
    path('accounts/registrar', Registrar, name='registrar'),
    # path('crear_modalidad', ModalityCreate.as_view(), name='create-modality'),
    # path('crear_evento', EventCreate.as_view(), name='create-event'),
    path('crear_artista', ArtistCreate.as_view(), name='create-artista'),
    path('crear_obra', ObraCreate.as_view(), name='create-obra'),
    path('formularios/artista_form/<int:pk>/', UpdateArtista.as_view(), name='upd-artista'),
    path('formularios/obra_form/<int:pk>/', UpdateObra.as_view(), name='upd-obra'),
    # path('formularios/modalidad_form/<int:pk>/', UpdateModality.as_view(), name='upd-modality'),
    # path('formularios/eventos_form/<int:pk>/', UpdateEvento.as_view(), name='upd-eventos'),
    path('eliminar_artista/<int:pk>', EliminarArtista.as_view(), name='dlt-artista'),
    path('eliminar_obra/<int:pk>', EliminarObra.as_view(), name='dlt_obra')
]
