from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import *
from .forms import *
from django.urls import reverse

# Teste para Validação de Formulários:
class GameFormTest(TestCase):
    def setUp(self):
        self.enterprise = Enterprise.objects.create(enterprise_name="Test Enterprise", enterprise_year=2000)
        self.publisher = Publisher.objects.create(
            enterprise_pub=self.enterprise,
            publisher_name="Test Publisher", 
            publisher_year=2005
        )
        self.dev = Dev.objects.create(
            dev_name="Test Dev", 
            dev_last_name="Test Lastname", 
            dev_nickname="DevTest", 
            dev_years=3
        )

    def test_form_valid(self):
        # Dados válidos para o formulário
        form_data = {
            'title_game': 'Test Game',
            'year_game': 2022,
            'game_star': 3,  # "BOM"
            'publisher_game': self.publisher.id,  
            'enterprise_game': self.enterprise.id,  
            'devs_game': [self.dev.id], 
        }
        form = GameForm(data=form_data)
        
        self.assertTrue(form.is_valid())

        
# Teste para Validação dos Modelos:

class EnterpriseModelTest(TestCase):
    def test_create_enterprise(self):
        enterprise = Enterprise.objects.create(enterprise_name="Test Enterprise", enterprise_year=2000)
        self.assertEqual(enterprise.enterprise_name, "Test Enterprise")
        self.assertEqual(enterprise.enterprise_year, 2000)

    def test_enterprise_name_max_length(self):
        enterprise = Enterprise.objects.create(enterprise_name="A" * 30, enterprise_year=2020)
        self.assertEqual(len(enterprise.enterprise_name), 30)

    def test_enterprise_year_positive(self):
        enterprise = Enterprise.objects.create(enterprise_name="Valid Enterprise", enterprise_year=2021)
        self.assertTrue(enterprise.enterprise_year > 0)


class PublisherModelTest(TestCase):
    def setUp(self):
        self.enterprise = Enterprise.objects.create(enterprise_name="Enterprise Test", enterprise_year=1995)

    def test_create_publisher(self):
        publisher = Publisher.objects.create(enterprise_pub=self.enterprise, publisher_name="Test Publisher", publisher_year=2005)
        self.assertEqual(publisher.publisher_name, "Test Publisher")
        self.assertEqual(publisher.publisher_year, 2005)
        self.assertEqual(publisher.enterprise_pub, self.enterprise)

    def test_publisher_name_max_length(self):
        publisher = Publisher.objects.create(enterprise_pub=self.enterprise, publisher_name="A" * 30, publisher_year=2020)
        self.assertEqual(len(publisher.publisher_name), 30)

class DevModelTest(TestCase):
    def setUp(self):
        self.enterprise = Enterprise.objects.create(enterprise_name="Test Enterprise", enterprise_year=2000)

    def test_create_dev(self):
        dev = Dev.objects.create(dev_name="John", dev_last_name="Doe", dev_nickname="Johnny", dev_years=5)
        dev.enterprises.add(self.enterprise)
        self.assertEqual(dev.dev_name, "John")
        self.assertEqual(dev.dev_last_name, "Doe")
        self.assertEqual(dev.dev_nickname, "Johnny")
        self.assertEqual(dev.dev_years, 5)
        self.assertIn(self.enterprise, dev.enterprises.all())

class GameModelTest(TestCase):
    def setUp(self):
        self.enterprise = Enterprise.objects.create(
            enterprise_name="Test Enterprise", 
            enterprise_year=2000
        )
        
        self.publisher = Publisher.objects.create(
            enterprise_pub=self.enterprise, 
            publisher_name="Test Publisher", 
            publisher_year=2005
        )
        
        self.dev = Dev.objects.create(
            dev_name="John", 
            dev_last_name="Doe", 
            dev_nickname="Johnny", 
            dev_years=5
        )
        
        self.assertIsNotNone(self.publisher)  

        self.game = Game.objects.create(
            title_game="Test Game",
            year_game=2022,
            game_star=3,  # "BOM"
            publisher_game=self.publisher,  
            enterprise_game=self.enterprise 
        )
        
        # Associando o Dev ao Game
        self.game.devs_game.add(self.dev)

    def test_create_game(self):
        # Verificando se o Game foi criado corretamente
        self.assertEqual(self.game.title_game, "Test Game")
        self.assertEqual(self.game.year_game, 2022)
        self.assertEqual(self.game.game_star, 3)  # "BOM"
        self.assertEqual(self.game.publisher_game, self.publisher)  # Verificando se o publisher foi associado
        self.assertEqual(self.game.enterprise_game, self.enterprise)  # Verificando se o enterprise foi associado
        self.assertIn(self.dev, self.game.devs_game.all())  # Verificando se o dev foi associado

    def test_game_star_choices(self):
        self.assertEqual(self.game.game_star, Game.Star_Values.BOM)



# Teste para Validar os Dados:

class GameValidationTest(TestCase):
    def setUp(self):
        self.enterprise = Enterprise.objects.create(enterprise_name="Test Enterprise", enterprise_year=2000)
    
        self.publisher = Publisher.objects.create(
            enterprise_pub=self.enterprise, 
            publisher_name="Test Publisher", 
            publisher_year=2005
        )
        
        self.dev = Dev.objects.create(
            dev_name="John", 
            dev_last_name="Doe", 
            dev_nickname="Johnny", 
            dev_years=5
        )

    def test_game_without_publisher(self):
        game = Game(
            title_game="Invalid Game",
            year_game=2022,
            game_star=3, 
            enterprise_game=self.enterprise
        )
        
        with self.assertRaises(ValidationError):
            game.full_clean()  

