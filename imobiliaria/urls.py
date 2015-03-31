from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'imobiliaria.views.home', name='home'),
    # url(r'^imobiliaria/', include('imobiliaria.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #url(r'^pesquisa/(?P<pagina>\d+)', 'programa.views.links'),

    #url(r'^pesquisando/', 'programa.views.links'),
    #url(r'^pesquisando/(?P<pagina>\d+)', 'programa.views.links'),
    #url(r'^pesquisa/', 'programa.views.pesquisa'),
    url(r'^pesquisa/', 'programa.views.pesquisa'),
    url(r'^contato/$', 'views.contato'),
    url(r'^listagem/', 'programa.views.listagem'), #PROCESSO DE EXPORTACAO DOS IMOVEIS

    #http://imoveisemfranca.com.br/pesquisa/www.c2imobiliaria.com.br/imovel-3229/vende-se-terreno-em-franca-no-bairro-santa-eugenia/

    # (r'^site_media/$', 'django.views.serve'),
    #url(r'^(?P<urlEnviada>\S+)/#/', 'programa.views.links'),
    url(r'^', 'programa.views.links'),
    url(r'^media(.*)$', 'django.views.static.serve',{ 'document_root' : settings.MEDIA_ROOT }),
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()