# -*- coding: utf8 -*-
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.template import RequestContext
from django import forms
from django.core.mail import send_mail, EmailMultiAlternatives
from programa.models import Empresa, Imovel, Fotos, Usuario
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import cache_page
from django.core.context_processors import csrf
from django.test import Client
from django.core.mail import send_mail
from django.http import HttpResponse
import codecs
csrf_client = Client(enforce_csrf_checks=True)


#MODO DE USAR
# http://localhost:8000/www.siteimobiliaria.com.br/cidade-franca
# http://localhost:8000/www.siteimobiliaria.com.br/tipo-terreno/cidade-franca
# http://localhost:8000/www.siteimobiliaria.com.br/bairro-centro
# http://localhost:8000/www.siteimobiliaria.com.br/tipo-terreno/bairro-centro/cidade-franca
# http://localhost:8000/www.siteimobiliaria.com.br/bairro-centro/cidade-franca/tipo-terreno/
# http://localhost:8000/www.siteimobiliaria.com.br/bairro-centro/cidade-ribeirao-preto/tipo-casa/
# http://localhost:8000/www.siteimobiliaria.com.br/bairro-centro/cidade-ribeirao-preto/tipo-casa/
# PARA LISTAR TUDO = # http://localhost:8000/www.siteimobiliaria.com.br/
#
# FICANDO ASSIM LINK DO IMOVEL DETALHADO
# http://localhost:8080/pesquisa/www.grupohabitat.com.br/imovel-10014110/aluga-se-casa-em-franca-no-bairro-parque-residencial-nova-franca

@csrf_exempt
def links(request):
	parametros = request.get_full_path().split('/')
	consulta = {} #CRIEI UM ARRAY COM OS PARÂMETROS
	imovelvalor = False
	ordem_por = False
	pesquisa = ""
	url = ''
	finalidade_busca = ''

	for dado in parametros:

		if dado.find('www.') >= 0:
			empresa = Empresa.objects.get(site=dado)
			#	UNICA BUSCA NO BANCO!
			imoveis = Imovel.objects.filter(id_empresa=empresa.id_empresa)

		if dado.find('ordenar-por-') >= 0:
			ordem_por = True
			url += '/' + dado
			por_ordem = dado.replace('ordenar-por-', '')
			pesquisa += " >> " + por_ordem

		if dado.find('cidade-') >= 0:
			url += '/' + dado
			dado = dado.replace('cidade-', '')
			consulta['cidade'] = dado.replace('-',' ').upper() #CONSULTA USANDO API DO DJANGO
			pesquisa += " >> " + consulta['cidade']

		if dado.find('bairro-') >= 0:
			url += '/' + dado
			dado = dado.replace('bairro-', '')
			consulta['bairro'] = dado.replace('-',' ').upper() #CONSULTA USANDO API DO DJANGO
			pesquisa += " >> " + consulta['bairro'] 

		if dado.find('tipo-') >= 0:
			url += '/' + dado
			dado = dado.replace('tipo-', '')
			consulta['tipo'] = dado.replace('-',' ').upper() #CONSULTA USANDO API DO DJANGO
			pesquisa += " >> " + consulta['tipo'] 

		if dado.find('dormitorios-') >= 0:
			url += '/' + dado
			dado = dado.replace('dormitorios-', '')
			consulta['dormitorios'] = dado.replace('-',' ').upper() #CONSULTA USANDO API DO DJANGO
			pesquisa += " >> " + consulta['dormitorios']

		if dado.find('texto-') >= 0:
			url += '/' + dado
			dado = dado.replace('texto-', '')
			consulta['texto'] = dado.replace('-',' ').upper() #CONSULTA USANDO API DO DJANGO
			pesquisa += " >> " + consulta['texto']

		if dado.find('finalidade-') >= 0:
			url += '/' + dado
			finalidade_busca = dado
			dado = dado.replace('finalidade-', '')
			consulta['finalidade'] = dado.replace('-',' ').upper() #CONSULTA USANDO API DO DJANGO
			pesquisa += " >> " + consulta['finalidade'] 

		if dado.find('codigo-') >= 0:
			url += '/' + dado
			dado = dado.replace('codigo-', '')
			consulta['cod_imovel'] = str(dado) #CONSULTA USANDO API DO DJANGO
			pesquisa += " >> " + consulta['cod_imovel']

		if dado.find('valor-') >= 0:
			url += '/' + dado
			valorimovel = dado.replace('valor-', '')
			imovelvalor = True
			pesquisa += " >> " + valorimovel

	tipo_temporada   = imoveis.filter(finalidade='TEMPORADA').values('tipo','finalidade').distinct().order_by('tipo')
	tipo_aluguel     = imoveis.filter(finalidade='ALUGUEL').values('tipo','finalidade').distinct().order_by('tipo')
	tipo_venda       = imoveis.filter(finalidade='VENDA').values('tipo','finalidade').distinct().order_by('tipo')
	cidade           = imoveis.values('cidade').distinct().order_by('cidade')
	bairro           = imoveis.values('bairro').distinct().order_by('bairro')
	valor            = imoveis.values('valor').distinct().order_by('valor')
	dormitorios      = imoveis.values('dormitorios').distinct().order_by('dormitorios')

	if imovelvalor == True:
		if valorimovel == 'ate-50-mil':
			imoveis = imoveis.filter(valor__lte=50000.00)

		elif valorimovel == '50-mil-100-mil':
			imoveis = imoveis.filter(valor__gt=50000.00,  valor__lte=100000.00)

		elif valorimovel == '100-mil-300-mil':
			imoveis = imoveis.filter(valor__gt=100000.00,  valor__lte=300000.00)

		elif valorimovel == '300-mil-500-mil':
			imoveis = imoveis.filter(valor__gt=300000.00,  valor__lte=500000.00)
		
		elif valorimovel == 'mais-de-500-mil':
			imoveis = imoveis.filter(valor__gte=500000.00)

	if ordem_por == True:
		if por_ordem == 'finalidadebusca':
			imoveis = imoveis.filter(**consulta).order_by('finalidade')

		elif por_ordem == 'tipobusca':
			imoveis = imoveis.filter(**consulta).order_by('tipo')
		
		elif por_ordem == 'cidadebusca':
			imoveis = imoveis.filter(**consulta).order_by('cidade')
		
		elif por_ordem == 'bairrobusca':
			imoveis = imoveis.filter(**consulta).order_by('bairro')

		elif por_ordem == 'quartosmenos':
			imoveis = imoveis.filter(**consulta).order_by('dormitorios')

		elif por_ordem == 'quartosmais':
			imoveis = imoveis.filter(**consulta).order_by('-dormitorios')
		
		elif por_ordem == 'valormaior':
			imoveis = imoveis.filter(**consulta).order_by('-valor')
		
		elif por_ordem == 'valormenor':
			imoveis = imoveis.filter(**consulta).order_by('valor')
		#paginator = Paginator(imoveis, 10)
	else:
		imoveis = imoveis.filter(**consulta).order_by('-valor')
		#paginator = Paginator(imoveis.filter(**consulta).order_by('-valor'), 10)

	paginator = Paginator(imoveis, 10)

	page = request.GET.get('page')
	try:
		imoveis = paginator.page(page)
	except PageNotAnInteger:
		imoveis = paginator.page(1)
	except EmptyPage:
		imoveis = paginator.page(paginator.num_pages)

	num_pages = []
	for p in range(paginator.num_pages):
		num_pages.append(p+1)
    
	return render_to_response('index.html', {
		'imoveis':imoveis,
        'num_pages': num_pages,
		'empresa':empresa,
		'dormitorios': dormitorios,
		'tipo_temporada': tipo_temporada,
		'tipo_aluguel': tipo_aluguel,
		'tipo_venda': tipo_venda,
		'cidade': cidade,
		'bairro': bairro,
		'valor': valor,
		'pesquisa':pesquisa,
		'url': url,
		'finalidade_busca': finalidade_busca
		})


@csrf_exempt
def pesquisa(request):
	parametros = request.get_full_path().split('/')
	consulta = {} #CRIEI UM ARRAY COM OS PARÂMETROS

	for dado in parametros:
		if dado.find('www.') >= 0:
			empresa = Empresa.objects.get(site=dado)

		if dado.find('imovel-') >= 0:
				id = dado.replace('imovel-', '')
				imovel = Imovel.objects.get(cod_imovel=id, id_empresa=empresa.id_empresa)
	
	imoveis_relacionados =  Imovel.objects.filter(finalidade=imovel.finalidade, tipo=imovel.tipo, cidade=imovel.cidade).order_by('-valor')[:4]

	if request.method == 'POST':
		if request.POST['nome']:
			nome = request.POST['nome']

		if request.POST['telefone']:
			telefone = request.POST['telefone'] 

		if request.POST['emailUsuario']:
			emailusuario = request.POST['emailUsuario']

		if request.POST['mensagem']:
			mensagem = request.POST['mensagem'] 

		subject, from_email, to = '=> EMAIL DO SEU SITE', 'lucas@celuladigital.com.br', 'lucas@celuladigital.com.br'

		html_content = render_to_string('sendmail.html', {'nome':nome,
		  'telefone': telefone,
		  'email':emailusuario,
		  'imoveis':imoveis,
		  'empresa':empresa,
		  'mensagem': mensagem})

		text_content = strip_tags(html_content)
		msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
		msg.attach_alternative(html_content, "text/html")
		msg.send()

	return render_to_response('imovel.html', {
		'imovel': imovel,
		'imoveis_relacionados':imoveis_relacionados,
		'empresa':empresa
	})
