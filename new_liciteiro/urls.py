from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from app_objeto.views import *
from app_cnaes.views import *
from app_categoria_arquivos.views import *
from app_fontes.views import *
from app_empresa.views import *
from app_licitacao.views import *
from app_orgao.views import *
from app_uf_cidades.views import *
from dashboard.views import *

urlpatterns = [
     url(r'^admin/', admin.site.urls),
     url(r'^$', dashboard_index),
     url(r'^cria_empresa/',CriaEmpresa),
     url(r'^lista_empresa/',Lista_empresas),
     url(r'^item_empresa/(?P<nr_item>\d+)/$',Detalha_empresa),
     url(r'^cria_objeto/',Cria_Objeto),
     url(r'^cria_categoria_arquivos',Cria_categoria_arquivos),
     url(r'^cria_fonte',Cria_fontes),
     url(r'^cria_atos_licitacao',Cria_Ato_licitacao),
     url(r'^cria_modalidade_licitacao',Cria_Modalidade_licitacao),
     url(r'^cria_tipos_licitacao',Cria_Tipo_licitacao),
     url(r'^cria_orgao', Cria_orgao),
     url(r'^cria_cidade', Cria_cidade),
     url(r'^cria_estado', Cria_estado),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)