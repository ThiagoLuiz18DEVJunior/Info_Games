from django.urls import path
from .views import *
from .user_view import *


urlpatterns = [
   path('', home_page, name='home'),
   path('register/', register, name='register'),
   path('login/', login_info_games, name='login'),
   path('logout/', logout_info_games, name='logout'),
   path('listar/', DataList.as_view(), name='listar'),
   path('detalhar/', DataListDetails.as_view(), name='detalhar'),
   path('adicionar/', DataAdd.as_view(), name='adicionar'),
   path('atualizar/<str:model>/<int:pk>/', DataAtt.as_view(), name='atualizar'),
   path('empresa/excluir/<int:pk>/', excluir_emp, name='excluir_empresas'), 
   path('dev/excluir/<int:pk>/', excluir_dev, name='excluir_dev'), 
   path('publisher/excluir/<int:pk>/', excluir_pub, name='excluir_publisher'), 
   path('games/excluir/<int:pk>/', excluir_jogos, name='excluir_jogos'), 
]
