from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
class CustomUser(AbstractUser):
    # Adicione related_name para evitar o conflito
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Define um nome relacionado único para evitar conflito
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Define um nome relacionado único para evitar conflito
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )
    from django.db import models

class Doador(models.Model):
    nome = models.CharField(max_length=100)
    contato = models.CharField(max_length=100, blank=True, null=True)
    usuario = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)  # Assume que cada doador é um usuário
    def __str__(self):
        return self.nome

class Doacao(models.Model):
    doador = models.ForeignKey(Doador, on_delete=models.CASCADE)
    tipo_material = models.CharField(max_length=100)
    quantidade = models.PositiveIntegerField()
    data_doacao = models.DateField(auto_now_add=True)
    produto = models.CharField(max_length=255, default='Produto Não Especificado')
    def __str__(self):
        return f"{self.tipo_material} - {self.doador.nome}"


