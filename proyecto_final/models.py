from django.db import models


# Create your models here.


class Artista(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    ci = models.IntegerField()
    grupo = models.IntegerField()
    sexo = models.CharField(max_length=10)


class Obra(models.Model):
    nombre = models.CharField(max_length=50)
    genero = models.CharField(max_length=15)
    duracion = models.DurationField()
    autor = models.CharField(max_length=50)


class Evento_resultado(models.Model):
    nombre_artista = models.CharField(max_length=50)
    nombre_obra = models.CharField(max_length=50)
    modalidad = models.CharField(max_length=15)
    resultado = models.CharField(max_length=10)


class Modalidad(models.Model):
    modalidad = models.CharField(max_length=15)
