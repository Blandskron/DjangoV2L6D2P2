from django.db import models

class Leccion(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_publicacion = models.DateField()
    duracion_minutos = models.IntegerField()
    archivo = models.FileField(upload_to='archivos_lecciones/', null=True, blank=True)

    def __str__(self):
        return self.titulo