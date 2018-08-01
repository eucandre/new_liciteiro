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
     url(r'^edita_empresa/(?P<nr_item>\d+)/$',edita_empresa),
     url(r'^cria_objeto/',Cria_Objeto),
     url(r'^lista_objeto/',Lista_objetos),
     url(r'^item_objeto/(?P<nr_item>\d+)/$',item_objeto),
     url(r'^edita_objeto/(?P<nr_item>\d+)/$',edita_objeto),
     url(r'^cria_categoria_arquivos',Cria_categoria_arquivos),
     url(r'^edita_categoria_arquivos/(?P<nr_item>\d+)/$',edita_categoria_arquivos),
     url(r'^lista_categoria_arquivos',lista_categorias_arquivos),
     url(r'^item_categoria_arquivos/(?P<nr_item>\d+)/$',item_categorias_arquivos),
     url(r'^cria_fonte',Cria_fontes),
     url(r'^edita_fonte/(?P<nr_item>\d+)/$',edita_fonte),
     url(r'^lista_fontes',Lista_fontes),
     url(r'^item_fontes/(?P<nr_item>\d+)/$',item_fonte),
     url(r'^cria_atos_licitacao/',Cria_Ato_licitacao),
     url(r'^lista_atos_licitacao',Lista_ato_licitacao),
     url(r'^item_ato_licitacao/(?P<nr_item>\d+)/$',item_ato_licitacao),
     url(r'^edita_ato_licitacao/(?P<nr_item>\d+)/$',edita_Ato_licitacao),
     url(r'^cria_modalidade_licitacao',Cria_Modalidade_licitacao),
     url(r'^lista_modalidades_licitacao',Lista_modalidade_licitacao),
     url(r'^item_modalidade_licitacao/(?P<nr_item>\d+)/$',item_modalidade_licitacao),
     url(r'^edita_modalidade_licitacao/(?P<nr_item>\d+)/$',edita_Modalidade_licitacao),
     url(r'^cria_tipos_licitacao',Cria_Tipo_licitacao),
     url(r'^lista_tipos_licitacao',Lista_tipo_licitacao),
     url(r'^item_tipo_licitacao/(?P<nr_item>\d+)/$',item_tipo_licitacao),
     url(r'^edita_tipo_licitacao/(?P<nr_item>\d+)/$',edita_Tipo_licitacao),
     url(r'^cria_orgao', Cria_orgao),
     url(r'^lista_orgaos',Lista_orgaos),
     url(r'^item_orgao/(?P<nr_item>\d+)/$',item_orgao),
     url(r'^edita_orgao/(?P<nr_item>\d+)/$',edita_orgao),
     url(r'^cria_cidade', Cria_cidade),
     url(r'^lista_cidade',Lista_cidades),
     url(r'^item_cidade/(?P<nr_item>\d+)/$',item_cidades),
     url(r'^edita_cidade/(?P<nr_item>\d+)/$',edita_cidade),
     url(r'^cria_estado', Cria_estado),
     url(r'^lista_estados',Lista_estados),
     url(r'^item_estado/(?P<nr_item>\d+)/$',item_estados),
     url(r'^edita_estado/(?P<nr_item>\d+)/$',edita_estado),
     url(r'^cria_cnaes_divisoes', Cria_cnaes_divisoes),
     url(r'^lista_cnaes_divisoes',lista_cnaes_divisoes),
     url(r'^item_cnae_divisoes/(?P<nr_item>\d+)/$',item_cnaes_divisoes),
     url(r'^edita_cnae_divisoes/(?P<nr_item>\d+)/$',edita_cnaes_divisoes),
  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)