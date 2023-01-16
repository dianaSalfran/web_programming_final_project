from django.db import models


# Create your models here.


class Artista(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    ci = models.IntegerField(max_length=11, unique=True)
    grupo = models.IntegerField()
    sexo = models.CharField(max_length=10)

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellidos}"

    class Meta:
        verbose_name = 'Artista'
        verbose_name_plural = 'Artistas'


class Obra(models.Model):
    nombre = models.CharField(max_length=50)
    genero = models.CharField(max_length=15)
    duracion = models.DurationField()
    autor = models.ManyToManyField(Artista, blank=True)
    modalidad = models.CharField(max_length=15)
    resultado = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.nombre
    
    @property
    def nombre_autores(self):
        return ";".join([a.nombre for a in self.autor.all()])

    class Meta:
        verbose_name = 'Obra'
        verbose_name_plural = 'Obras'


# class Evento_resultado(models.Model):
#     nombre_artista = models.CharField(max_length=50)
#     nombre_obra = models.CharField(max_length=50)
#     modalidad = models.CharField(max_length=15)
#     resultado = models.CharField(max_length=10)


# class Modalidad(models.Model):
#     modalidad = models.CharField(max_length=15)
