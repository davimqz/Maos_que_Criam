from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Doacao, Doador, Feedback, Necessidade
from datetime import datetime
from django.contrib.auth import logout
from django.utils.dateparse import parse_date
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import folium


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

def necessidades_view(request):
    necessidades = Necessidade.objects.all().order_by('-data_criacao')  # Ordena pela data de criação
    return render(request, 'necessidades-especificas.html', {'necessidades': necessidades})

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from .models import FAQ, FAQResponse
from django.views.decorators.csrf import csrf_exempt
import json

def faq_list(request):
    """Exibe a lista de perguntas frequentes."""
    faqs = FAQ.objects.all()
    return render(request, 'faq_list.html', {'faqs': faqs})


@csrf_exempt
def submit_response(request, faq_id):
    """Recebe e armazena a resposta do usuário para uma pergunta específica."""
    if request.method == 'POST':
        try:
            faq = get_object_or_404(FAQ, id=faq_id)
            data = json.loads(request.body)
            user_response = data.get('response')

            if not user_response:
                return JsonResponse({'error': 'A resposta não pode estar vazia.'}, status=400)

            FAQResponse.objects.create(faq=faq, user_response=user_response)
            return JsonResponse({'message': 'Resposta enviada com sucesso.'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return HttpResponse('Método não permitido.', status=405)
    
from django.shortcuts import render, redirect
from .models import Pergunta

# Exibe as perguntas frequentes
def perguntas_frequentes(request):
    perguntas = Pergunta.objects.all().order_by('-data_criacao')  # Ordena por data, mais recente primeiro
    return render(request, 'perguntas_frequentes.html', {'perguntas': perguntas})

# Lida com o envio de novas perguntas
def enviar_pergunta(request):
    if request.method == 'POST':
        texto = request.POST.get('pergunta')  # Obtém o texto da pergunta do formulário
        if texto:
            Pergunta.objects.create(texto=texto)  # Cria a pergunta no banco de dados
        return redirect('perguntas_frequentes')  # Redireciona para a página de perguntas
    return render(request, 'enviar_pergunta.html')

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404, redirect, render
from .models import Pergunta

# Verifica se o usuário é administrador
def is_admin(user):
    return user.is_staff

@user_passes_test(is_admin)
def gerenciar_perguntas(request):
    perguntas = Pergunta.objects.all().order_by('-data_criacao')

    if request.method == 'POST':
        pergunta_id = request.POST.get('pergunta_id')
        resposta = request.POST.get('resposta')

        pergunta = get_object_or_404(Pergunta, id=pergunta_id)
        pergunta.resposta = resposta
        pergunta.save()

        return redirect('gerenciar_perguntas')

    return render(request, 'gerenciar_perguntas.html', {'perguntas': perguntas})


def historico_doacoes(request):
    feedbacks = Feedback.objects.all().order_by('-id')  # Ordena por ordem decrescente de criação
    return render(request, 'historico-doacoes.html', {'feedbacks': feedbacks})

def map_view(request):
    # Criação do mapa centralizado
    mapa = folium.Map(location=[-8.047562, -34.877], zoom_start=12)

    # Lista de pontos de coleta
    pontos = [
        {
            "nome": "Espaço 46",
            "endereco": "Av. República do Líbano, 251, RioMar Shopping, Piso L2",
            "latitude": -8.08581,
            "longitude": -34.89477,
            "cor": "blue",  # Cor do marcador
        },
    ]

    # Adiciona marcadores ao mapa
    for ponto in pontos:
        # HTML do pop-up com links corrigidos
        popup_html = f"""
        <b>{ponto['nome']}</b><br>
        {ponto['endereco']}<br>
        <a href="https://www.google.com/maps/dir/?api=1&destination={ponto['latitude']},{ponto['longitude']}" target="_blank">
            Rota no Google Maps
        </a><br>
        <a href="https://www.openstreetmap.org/directions?to={ponto['latitude']},{ponto['longitude']}" target="_blank">
            Rota no OpenStreetMap
        </a>
        """
        folium.Marker(
            location=[ponto["latitude"], ponto["longitude"]],
            popup=popup_html,
            tooltip=ponto["nome"],
            icon=folium.Icon(color=ponto["cor"]),  # Define a cor do marcador
        ).add_to(mapa)

    # Renderiza o mapa como HTML
    mapa_html = mapa._repr_html_()

    # Passa o mapa e os pontos para o template
    return render(request, "mapeamento.html", {"mapa": mapa_html})