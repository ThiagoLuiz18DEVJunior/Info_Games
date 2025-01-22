from django.db import models
from datetime import datetime
from django.forms import ValidationError

# Create your models here.
# Usei a tabela abaixo de exemplo com base no material disponivel
"""class Person(models.Model):
   first_name = models.CharField(max_length=30)
   last_name = models.CharField(max_length=30)
"""   
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

    publisher_game = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    enterprise_game = models.ForeignKey(Enterprise, on_delete=models.CASCADE)
    devs_game =  models.ManyToManyField(Dev)
    game_star = models.IntegerField(choices=Star_Values.choices)
    title_game = models.CharField(max_length=30)
    year_game = models.PositiveIntegerField()

    def clean(self):
        actual_year = datetime.now().year
        if self.year_game > actual_year:
            raise ValidationError(f"O ano do jogo não pode ser maior que o ano atual ({actual_year}).")

    def __str__(self):
        devs_names = ", ".join(dev.dev_name for dev in self.devs_game.all())
        return f"{self.title_game} ({self.year_game}) - {self.enterprise_game} - {self.publisher_game} - Devs: {devs_names}"
    
    def get_stars(self):
        return '★' * self.game_star + '☆' * (5 - self.game_star)

# Dados Adicionados via Shell (CRUD) (comando: python manage.py shell)
# Comandos e comentários do desenvolvedor. 
# Optei por usar dados ficticios, coletados via IA (ChatGPT), facilitou os testes do BD SQlite. 

"""
from games.models import Enterprise, Publisher, Dev, Game

# Criando algumas empresas fictícias
enterprise1 = Enterprise.objects.create(enterprise_name="Super Games", enterprise_year=2005)
enterprise2 = Enterprise.objects.create(enterprise_name="Pixel Studios", enterprise_year=2012)

# Criando alguns publishers fictícios
publisher1 = Publisher.objects.create(enterprise_pub=enterprise1, publisher_name="Mega Publishing", publisher_year=2010)
publisher2 = Publisher.objects.create(enterprise_pub=enterprise2, publisher_name="Future Entertainment", publisher_year=2015)

# Criando alguns desenvolvedores fictícios
dev1 = Dev.objects.create(dev_name="Carlos", dev_last_name="Almeida", dev_nickname="CarlosDev", dev_years=7)
dev2 = Dev.objects.create(dev_name="Maria", dev_last_name="Silva", dev_nickname="SilvaM", dev_years=5)
dev3 = Dev.objects.create(dev_name="João", dev_last_name="Costa", dev_nickname="Joaozinho", dev_years=10)

# Associando desenvolvedores a empresas
enterprise1.devs_set.add(dev1, dev2)
enterprise2.devs_set.add(dev2, dev3)

# Criando alguns jogos fictícios
game1 = Game.objects.create(
    publisher_game=publisher1,
    enterprise_game=enterprise1,
    title_game="Epic Adventure",
    year_game=2018,
    game_star=5
)
game1.devs_game.add(dev1, dev2)

game2 = Game.objects.create(
    publisher_game=publisher2,
    enterprise_game=enterprise2,
    title_game="Pixel Runner",
    year_game=2020,
    game_star=4
)
game2.devs_game.add(dev2, dev3)

game3 = Game.objects.create(
    publisher_game=publisher1,
    enterprise_game=enterprise1,
    title_game="Space Quest",
    year_game=2022,
    game_star=3
)
game3.devs_game.add(dev1)

# Conferindo se os dados foram inseridos corretamente
print(f"Empresas: {Enterprise.objects.all()}")
print(f"Publishers: {Publisher.objects.all()}")
print(f"Desenvolvedores: {Dev.objects.all()}")
print(f"Jogos: {Game.objects.all()}")

# Testei o Banco de Dados, deixei funcional, com as relações propostas no material e organizado com o DBeaver, só rodar e testar. 
"""

"""
-------------------- Criando diretamente no SQL ------------------------

# Criando as Tabelas:

CREATE TABLE Enterprise (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    enterprise_name TEXT NOT NULL,
    enterprise_year INTEGER NOT NULL
);

CREATE TABLE Publisher (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    enterprise_pub INTEGER,
    publisher_name TEXT NOT NULL,
    publisher_year INTEGER NOT NULL,
    FOREIGN KEY (enterprise_pub) REFERENCES Enterprise(id)
);

CREATE TABLE Dev (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dev_name TEXT NOT NULL,
    dev_last_name TEXT NOT NULL,
    dev_nickname TEXT NOT NULL,
    dev_years INTEGER NOT NULL
);

CREATE TABLE Game (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    publisher_game INTEGER,
    enterprise_game INTEGER,
    game_star INTEGER NOT NULL,
    title_game TEXT NOT NULL,
    year_game INTEGER NOT NULL,
    FOREIGN KEY (publisher_game) REFERENCES Publisher(id),
    FOREIGN KEY (enterprise_game) REFERENCES Enterprise(id)
);

CREATE TABLE Game_Dev (
    game_id INTEGER,
    dev_id INTEGER,
    PRIMARY KEY (game_id, dev_id),
    FOREIGN KEY (game_id) REFERENCES Game(id),
    FOREIGN KEY (dev_id) REFERENCES Dev(id)
);

# Testando pra ver se funciona (DBeaver)

INSERT INTO Enterprise (enterprise_name, enterprise_year) 
VALUES ('Game Studios', 2000);

# Como fiz direto via terminal o nome vai ser diferente devido ao comando Startapp e o nome do diretório:

INSERT INTO games_enterprise (enterprise_name, enterprise_year) 
VALUES ('Game Studios', 2000); 

# Consulta - Retorna os dados da nossa tabela:

SELECT * FROM games_enterprise;

# Update  - Atualizando um dado dentro da tabela:

UPDATE games_enterprise 
SET enterprise_name = 'ABC Games' 
WHERE id = 1;

# Delete - Para apagar um dado da nossa tabela (Muito cuidado estágiario!)

DELETE FROM games_enterprise  
WHERE id = 1;

# Todos esses comandos que mostrei podem ser utilizados para as demais tabelas, contanto que utilize
os seus respectivos valores armazenados na memória. 
"""