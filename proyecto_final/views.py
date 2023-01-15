from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, ListView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from urllib import request
from .models import Modalidad, Evento_resultado, Artista, Obra
from .forms import CustomUserForm, ArtistaForm, EventoForm, ObraForm, ModalidadForm


# Create your views here.


class Home(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'


class Artista(LoginRequiredMixin, ListView):
    model = Artista
    template_name = 'artista.html'


class ArtistCreate(LoginRequiredMixin, CreateView):
    model = Artista
    template_name = 'crear_artista.html'
    form_class = ArtistaForm

    def get_success_url(self):
        return reverse('artista')


class Obra(LoginRequiredMixin, ListView):
    model = Obra
    template_name = 'obra.html'


class ObraCreate(LoginRequiredMixin, CreateView):
    model = Obra
    template_name = 'crear_obra.html'
    form_class = ObraForm

    def get_success_url(self):
        return reverse('obra')


class Modality(LoginRequiredMixin, ListView):
    model = Modalidad
    template_name = 'modalidad.html'


class ModalityCreate(LoginRequiredMixin, CreateView):
    model = Modalidad
    template_name = 'crear_modalidad.html'
    form_class = ModalidadForm

    def get_success_url(self):
        return reverse('modalidad')


class Eventos(LoginRequiredMixin, ListView):
    model = Evento_resultado
    template_name = 'eventos.html'


class EventCreate(LoginRequiredMixin, CreateView):
    model = Evento_resultado
    template_name = 'crear_evento.html'
    form_class = EventoForm

    def get_success_url(self):
        return reverse('eventos')


def Registrar(request):
    data = {
        'form': CustomUserForm()
    }

    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
    return render(request, 'registration/registrar.html', data)


class UpdateArtista(LoginRequiredMixin, UpdateView):
    model = Artista
    form_class = ArtistaForm
    template_name = 'formularios/artista_form.html'
    success_url = reverse_lazy('artista')


class UpdateObra(LoginRequiredMixin, UpdateView):
    model = Obra
    form_class = ObraForm
    template_name = 'formularios/obra_form.html'

    def get_success_url(self):
        return reverse('obra')


class UpdateModality(LoginRequiredMixin, UpdateView):
    model = Modalidad
    form_class = ModalidadForm
    template_name = 'formularios/modalidad_form.html'

    def get_success_url(self):
        return reverse('modalidad')


class UpdateEvento(LoginRequiredMixin, UpdateView):
    model = Evento_resultado
    form_class = EventoForm
    template_name = 'formularios/eventos_form.html'

    def get_success_url(self):
        return reverse('eventos')


class EliminarArtista(LoginRequiredMixin, DeleteView):
    model = Artista
    template_name = 'eliminar_artista.html'
    success_url = reverse_lazy('artista')


class EliminarObra(LoginRequiredMixin, DeleteView):
    model = Obra
    template_name = 'eliminar_obra.html'
    success_url = reverse_lazy('obra')
