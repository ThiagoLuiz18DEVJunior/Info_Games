from django.urls import path
from .views import *

urlpatterns = [
   path('', home_page, name="home"),

   # Path pra config de DB da Empresa
   path('empresa/', listar_emp, name='listar_empresas'),
   path('empresa/adicionar/', add_emp , name='adicionar_empresas'), 
   path('empresa/editar/<int:pk>/', atualizar_emp, name='atualizar_empresas'), 
   path('empresa/detalhar/<int:pk>/', detalhar_emp, name='detalhar_empresas'), 
   path('empresa/excluir/<int:pk>/', excluir_emp, name='excluir_empresas'), 

   # Path pra config dos Desenvolvedores
   path('dev/', listar_devs, name='listar_devs'),
   path('dev/adicionar/', add_dev , name='adicionar_dev'), 
   path('dev/editar/<int:pk>/', atualizar_dev, name='atualizar_dev'), 
   path('dev/detalhar/<int:pk>/', detalhar_dev, name='detalhar_dev'), 
   path('dev/excluir/<int:pk>/', excluir_dev, name='excluir_dev'), 

   # Path pra config das Publisher
   path('publisher/', listar_pub, name='listar_pubs'),
   path('publisher/adicionar/', add_pub , name='adicionar_publisher'), 
   path('publisher/editar/<int:pk>/', atualizar_pub, name='atualizar_publisher'), 
   path('publisher/detalhar/<int:pk>/', detalhar_pub, name='detalhar_publisher'), 
   path('publisher/excluir/<int:pk>/', excluir_pub, name='excluir_publisher'), 

   # Path pra config de DB dos Jogos 
   path('games/', listar_jogos, name='listar_jogos'), 
   path('games/adicionar/', add_jogos , name='adicionar_jogos'), 
   path('games/editar/<int:pk>/', atualizar_jogos, name='atualizar_jogos'), 
   path('games/detalhar/<int:pk>/', detalhar_jogos, name='detalhar_jogos'), 
   path('games/excluir/<int:pk>/', excluir_jogos, name='excluir_jogos'), 
]
