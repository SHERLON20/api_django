from django.db import models
class categoria(models.Model):
    nome = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome
class livros(models.Model):
    streaming_choices = (('AK','Amazon kindle'),('F','Fisico'))
    nome=models.CharField(max_length=50)
    streaming = models.CharField(max_length=2,choices=streaming_choices)
    nota = models.IntegerField(null=True,blank=True)
    comentarios = models.TextField(null=True,blank=True)
    categorias = models.ManyToManyField(categoria)
    
    def __str__(self):
        return self.nome