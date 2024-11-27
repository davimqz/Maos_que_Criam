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
    email = models.EmailField(max_length=100, blank=True, null=True)  # Novo atributo
    endereco = models.CharField(max_length=255, blank=True, null=True)  # Novo atributo
    usuario = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)  # Assume que cada doador é um usuário
    
    def __str__(self):
        return self.nome

class Doacao(models.Model):
    doador = models.ForeignKey(Doador, on_delete=models.CASCADE)
    tipo_material = models.CharField(max_length=100)
    quantidade = models.PositiveIntegerField()
    data_doacao = models.DateField(auto_now_add=True)
    produto = models.CharField(max_length=255, default='')
    def __str__(self):
        return f"{self.tipo_material} - {self.doador.nome}"


class Feedback(models.Model):
    nome = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    opiniao = models.TextField()
    avaliacao = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
    
from django.db import models

class Donor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    consent_to_share = models.BooleanField(default=True)  # Para controlar se o doador consente em compartilhar informações

    def __str__(self):
        return self.name

class Donation(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.SET_NULL, null=True)
    material_type = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()  # Quantidade doada
    date_donated = models.DateField(auto_now_add=True)  # Data da doação

    def __str__(self):
        return f"{self.material_type} - {self.quantity}"
    
class Necessidade(models.Model):
    item = models.CharField("Necessidade de Insumo", max_length=100)
    prioridade = models.CharField("Prioridade", max_length=20, choices=[('alta', 'Alta'), ('media', 'Média'), ('baixa', 'Baixa')])
    detalhes = models.TextField("Detalhes", blank=True, null=True)
    data_criacao = models.DateTimeField("Data de Criação", auto_now_add=True)

    def __str__(self):
        return f"{self.item} ({self.prioridade})"
    
from django.db import models

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question


class FAQResponse(models.Model):
    faq = models.ForeignKey(FAQ, on_delete=models.CASCADE, related_name="responses")
    user_response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Response to: {self.faq.question}"

class Pergunta(models.Model):
    texto = models.TextField("Pergunta")
    data_criacao = models.DateTimeField(auto_now_add=True)
    resposta = models.TextField("Resposta", blank=True, null=True)  # Campo para resposta
    def __str__(self):
        return self.texto[:50]  # Retorna os primeiros 50 caracteres