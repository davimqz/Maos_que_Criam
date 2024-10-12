from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Doacao, Doador
from datetime import datetime
from django.contrib.auth import logout
from django.utils.dateparse import parse_date
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error_message': 'Nome de usuário já existe.'})
        
        if User.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error_message': 'Email já cadastrado.'})

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, 'Usuário cadastrado com sucesso!')
        return redirect('login')  # Redireciona para a página de login ou outra página que você desejar.

    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login realizado com sucesso!')
            return redirect('home')  # Redireciona para uma página 'home' ou outra página após o login
        else:
            return render(request, 'login.html', {'error_message': 'Nome de usuário ou senha incorretos.'})

    return render(request, 'login.html')



def user_logout(request):
    logout(request)
    return redirect('login')  # Redireciona o usuário para a página de login após fazer logout


@login_required
def registrar_doacao(request):
    if request.method == 'POST':
        tipo_material = request.POST.get('tipo_material')
        quantidade = request.POST.get('quantidade')
        data_doacao = parse_date(request.POST.get('data_doacao'))
        doador = request.POST.get('doador')
        #produto = request.POST.get('produto')
        # Cria o objeto de doação e salva no banco de dados
        doacao = Doacao(
            tipo_material=tipo_material,
            quantidade=quantidade,
            data_doacao=data_doacao,
            doador = doador,
           
        )
        doacao.save()

        # Redireciona para uma página de sucesso ou volta à mesma página
        return redirect('pagina_de_sucesso')  # ou 'registrar_doacao'
    
    return render(request, 'registrar_doacao.html')
    
def lista_doacoes(request):
    doacoes = Doacao.objects.all()
    return render(request, 'lista_doacoes.html', {'doacoes': doacoes})

def home(request):
    return render(request, 'home.html')

 # Importar o modelo Doador


#def registrar_doacao_usuario(request):
   # if request.method == 'POST':
    #    usuario = request.user  # Assume que o usuário está autenticado
     #   quantidade = request.POST.get('quantidade')
      #  produto = request.POST.get('produto')

        # Verifica se o usuário tem um doador associado
       # try:
        #    doador = Doador.objects.get(usuario=usuario)
            # Criar nova doação
         #   Doacao.objects.create(doador=doador, produto=produto, quantidade=quantidade)
            # Redirecionar para uma página de sucesso ou lista de doações
          #  return redirect('home')  # Substitua pelo nome da URL da página de sucesso
        #except Doador.DoesNotExist:
         #   return render(request, 'registrar_doacao_usuario', {'mensagem': 'Doador não encontrado.'})

    # Para requisições GET, renderiza o formulário de doação
    #return render(request, 'registrar_doacao_usuario.html')







