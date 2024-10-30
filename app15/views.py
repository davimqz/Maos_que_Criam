from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Doacao, Doador, Feedback
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


def feedbackdoador(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        material = request.POST.get('material')
        opiniao = request.POST.get('opiniao')
        avaliacao = request.POST.get('opcoes')

        # Verifica se todos os campos foram preenchidos
        if nome and material and opiniao and avaliacao:
            # Cria e salva o feedback no banco de dados
            feedback = Feedback(nome=nome, material=material, opiniao=opiniao, avaliacao=avaliacao)
            feedback.save()
            return HttpResponse("Obrigado pelo seu feedback!")
        else:
            return HttpResponse("Por favor, preencha todos os campos.")

    return render(request, 'feedbackdoador.html')
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

from django.shortcuts import render
from django.http import HttpResponse
from .models import Donation
from django.utils import timezone
from django.template.loader import render_to_string
import csv
from reportlab.pdfgen import canvas
import io
from datetime import datetime
from django.core.exceptions import ValidationError 

def validate_date(date_text):
    try:
        return datetime.strptime(date_text, "%Y-%m-%d").date()
    except ValueError:
        raise ValidationError(f"'{date_text}' value has an invalid date format. It must be in YYYY-MM-DD format.")


# Função para gerar relatório em PDF
def generate_pdf_report(donations):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100, 750, "Relatório de Doações e Impacto Social")

    y = 700
    for donation in donations:
        line = f"Doador: {donation.donor.name}, Material: {donation.material_type}, Quantidade: {donation.quantity}, Data: {donation.date_donated}"
        p.drawString(100, y, line)
        y -= 20

    p.showPage()
    p.save()
    buffer.seek(0)
    return buffer

# View para gerar e exibir o relatório
def generate_report(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    material_type = request.GET.get('material_type')
    report_format = request.GET.get('format', 'html')

    # Inicializa a queryset de doações
    donations = Doacao.objects.all()

    # Filtra doações pela data de início e fim, se fornecidas
    if start_date:
        try:
            donations = donations.filter(data_doacao__gte=start_date)
        except ValidationError as e:
            return HttpResponse(f"Error: {e}")

    if end_date:
        try:
            donations = donations.filter(data_doacao__lte=end_date)
        except ValidationError as e:
            return HttpResponse(f"Error: {e}")

    # Filtra doações pelo tipo de material, se fornecido
    if material_type:
        donations = donations.filter(tipo_material__icontains=material_type)

    # Gera o relatório em HTML ou PDF
    if report_format == "pdf":
        response = HttpResponse(content_type="application/pdf")
        response["Content-Disposition"] = 'attachment; filename="relatorio_doacoes.pdf"'
        p = canvas.Canvas(response)

        # Título do relatório
        p.drawString(100, 800, "Relatório de Doações e Impacto Social")

        # Adicionar as informações de cada doação
        y_position = 750
        for donation in donations:
            donation_info = (
                f"Data: {donation.data_doacao}, "
                f"Material: {donation.tipo_material}, "
                f"Quantidade: {donation.quantidade}, "
                f"Doador: {donation.doador.nome}"
            )
            p.drawString(100, y_position, donation_info)
            y_position -= 20  # Move para a linha de baixo

            # Se alcançar o final da página, adicionar nova página
            if y_position < 50:
                p.showPage()
                y_position = 750

        p.showPage()
        p.save()
        return response

    # Para o formato HTML
    return render(request, "report.html", {"donations": donations})



