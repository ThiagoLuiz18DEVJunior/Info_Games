from django.db import models
from datetime import datetime
from django.forms import ValidationError
from django import forms
from django.contrib.auth.models import User

# Create your models here.
# Banco de Dados - Plataforma de Distribuição de Jogos Eletrônicos
# Separação do Banco - Empresa, Distribuidora, Desenvolvedores e Jogos.
   
class Enterprise (models.Model):
    enterprise_name = models.CharField(max_length=30)
    enterprise_year = models.PositiveIntegerField()

    def __str__(self):
      return f"{self.enterprise_name} ({self.enterprise_year})"

class Publisher (models.Model):
    enterprise_pub = models.ForeignKey(Enterprise, on_delete=models.CASCADE)
    publisher_name = models.CharField(max_length=30)
    publisher_year = models.PositiveIntegerField()

    def __str__(self):
      return f"{self.publisher_name} ({self.publisher_year})"

class Dev (models.Model):
    enterprises = models.ManyToManyField(Enterprise)
    dev_name = models.CharField(max_length=30)
    dev_last_name = models.CharField(max_length=30)
    dev_nickname = models.CharField(max_length=30)
    dev_years = models.PositiveIntegerField()

    def __str__(self):
      return f"{self.dev_name} {self.dev_last_name} ({self.dev_nickname})"

class Game (models.Model): 

    class Star_Values(models.IntegerChoices):
       MUITO_RUIM = 1, 'MUITO RUIM'
       RUIM = 2, 'RUIM'
       BOM = 3, 'BOM'
       MUITO_BOM = 4, 'MUITO BOM'
       EXCELENTE = 5, 'EXCELENTE'

    game_star = models.IntegerField(choices=Star_Values.choices)
    title_game = models.CharField(max_length=30)
    year_game = models.PositiveIntegerField()
    description_game = models.TextField(null=True, blank=True)
    devs_game =  models.ManyToManyField(Dev)
    publisher_game = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    enterprise_game = models.ForeignKey(Enterprise, on_delete=models.CASCADE)

    def clean(self):
        actual_year = datetime.now().year
        if self.year_game > actual_year:
            raise ValidationError(f"O ano do jogo não pode ser maior que o ano atual ({actual_year}).")

    def __str__(self):
        devs_names = ", ".join(dev.dev_name for dev in self.devs_game.all())
        return f"{self.title_game} ({self.year_game}) - {self.enterprise_game} - {self.publisher_game} - Devs: {devs_names}"
    
    def get_stars(self):
        return '★' * self.game_star + '☆' * (5 - self.game_star)

class UserForm (forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError("As senhas não coincidem.")
        return password2

