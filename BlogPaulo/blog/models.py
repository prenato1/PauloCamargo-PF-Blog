from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

class Page(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    subtitle = models.CharField(max_length=200, verbose_name="Subtítulo")
    content = RichTextUploadingField(verbose_name="Conteúdo")
    image = models.ImageField(upload_to='pages', verbose_name="Imagem")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização")
    published_date = models.DateField(auto_now_add=True, verbose_name="Data de Publicação")    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Página"
        verbose_name_plural = "Páginas"
        ordering = ['-created_at']
