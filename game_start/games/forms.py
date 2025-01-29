from django import forms
from .models import Game, Enterprise, Dev, Publisher


class GameForm(forms.ModelForm):
 class Meta:
    model = Game
    fields = [
      'game_star',
      'title_game', 
      'year_game', 
      'description_game',
      'devs_game',
      'enterprise_game',
      'publisher_game',
    ]

    labels = {
      'game_star': 'Avaliação do Jogo',  
      'title_game': 'Título do Jogo',  
      'year_game': 'Ano de Lançamento', 
      'description_game': 'Descrição do Jogo', 
      'devs_game': 'Desenvolvedores',  
      'enterprise_game': 'Empresa Criadora',  
      'publisher_game': 'Publisher', 
    }


class EnterpriseForm(forms.ModelForm):
 class Meta:
    model = Enterprise
    fields = [
      'enterprise_name',
      'enterprise_year',
    ]

    labels = {
      'enterprise_name': 'Nome da Empresa',
      'enterprise_year': 'Ano de Criação',
    }

class DevForm(forms.ModelForm):
 class Meta:
    model = Dev
    fields = [
      'dev_name',
      'dev_last_name',
      'dev_nickname',
      'dev_years',
      'enterprises',
    ]

    labels = {
      'dev_name': 'Nome',  
      'dev_last_name': 'Sobrenome',
      'dev_nickname': 'Apelido',
      'dev_years': 'Idade', 
      'enterprises': 'Empresas que Atuou',
    }
  
class PublisherForm(forms.ModelForm):
 class Meta:
    model = Publisher
    fields = [
      'publisher_name',
      'publisher_year',
      'enterprise_pub',
    ]

    labels = {
      'publisher_name': 'Nome da Publisher',
      'publisher_year': 'Ano de Criação',
      'enterprise_pub': 'Empresa Filiada',
    }
  
class UserForm(forms.ModelForm):
  class Meta:
    fields = [
      'password',
      'password2',
    ]