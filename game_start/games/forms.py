from django import forms
from .models import Game, Enterprise, Dev, Publisher


class GameForm(forms.ModelForm):
 class Meta:
    model = Game
    fields = [
      'game_star', 
      'title_game', 
      'year_game', 
      'devs_game',
      'enterprise_game',
      'publisher_game',
    ]

    widgets = {
    'devs_game' : forms.Select(attrs={'class': 'form-control'}),
    }

class EnterpriseForm(forms.ModelForm):
 class Meta:
    model = Enterprise
    fields = [
      'enterprise_name',
      'enterprise_year',
    ]

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
  
class PublisherForm(forms.ModelForm):
 class Meta:
    model = Publisher
    fields = [
      'publisher_name',
      'publisher_year',
      'enterprise_pub',
    ]
  
class UserForm(forms.ModelForm):
  class Meta:
    fields = [
      'password',
      'password2',
    ]