from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Page(models.Model):
    title = models.CharField("Título", max_length=100)
    subtitle = models.CharField("Subtítulo", max_length=100)
    content = RichTextField("Contenido")
    image = models.ImageField("Imagen destacada", upload_to='pages/')
    date = models.DateField("Fecha de publicación", auto_now_add=True)
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
