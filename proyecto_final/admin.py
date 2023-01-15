from django.contrib import admin

# Register your models here.
from proyecto_final.models import Modalidad, Artista, Obra, Evento_resultado

admin.site.register(Modalidad)
admin.site.register(Artista)
admin.site.register(Obra)
admin.site.register(Evento_resultado)
