from django.db import models

class Acessorio(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True)
    descricao = models.CharField(max_length=100, null=True, blank=True)
    quantidade = models.IntegerField()

    def __str__(self):
        return f"({self.id}) {self.nome}"
    

