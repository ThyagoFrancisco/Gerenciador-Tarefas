from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tarefa(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    concluida = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
    