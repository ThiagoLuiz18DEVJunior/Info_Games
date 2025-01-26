from django.shortcuts import *
from .user_view import *
from .models import Game, Enterprise, Publisher, Dev

def listar_dados(request):

    entity = request.GET.get('entity', 'games') 
    items_with_fields = []
    name_tbl = 'Game'
    

# Criando a Lista de Jogos:
    if entity == 'games':
        name_tbl = 'JOGOS'
        field_mapping = {
        'game_star': 'Avaliação',
        'title_game': 'Titulo do Jogo',
        'year_game': 'Ano de Lançamento',
        'devs_game': 'Desenvolvedores',
        'enterprise_game': 'Empresa',
        'publisher_game': 'Distribuidora',
        }

        items = Game.objects.all()
        item_pk = Game.objects.first()
        fields = [field.name for field in Game._meta.get_fields()]  

        for item in items:
            item_data = {}
            for field in Game._meta.get_fields():
                if field.concrete:
                    field_name = field.name
                    field_value = getattr(item, field_name)
                    if field_name in field_mapping:
                        item_data[field_mapping[field_name]] = field_value
                    else:
                        item_data[field_name] = field_value
            items_with_fields.append(item_data)

# Criando a Lista de Empresas:
    elif entity == 'enterprise':
        name_tbl = 'EMPRESAS'
        field_mapping = {
         'enterprise_name': 'Nome da Empresa',
         'enterprise_year': 'Ano de Criação',
        }

        items = Enterprise.objects.all()
        item_pk = Enterprise.objects.first()
        fields = [field.name for field in Enterprise._meta.get_fields()]  
        for item in items:
            item_data = {}
            for field in Enterprise._meta.get_fields():
                if field.concrete:
                    field_name = field.name
                    field_value = getattr(item, field_name)
                    if field_name in field_mapping:
                        item_data[field_mapping[field_name]] = field_value
                    else:
                        item_data[field_name] = field_value

            items_with_fields.append(item_data)

# Criando a Lista de Desenvolvedores:
    elif entity == 'dev':
        name_tbl = 'DESENVOLVEDORES'
        field_mapping = {
        'dev_name': 'Nome',
        'dev_last_name': 'Sobrenome',
        'dev_nickname':'Apelido',
        'dev_years': 'Idade',
        'enterprises': 'Empresas que Atuou',
        }

        items = Dev.objects.all()
        item_pk = Dev.objects.first()
        fields = [field.name for field in Dev._meta.get_fields()]  
        for item in items:
            item_data = {}
            for field in Dev._meta.get_fields():
                if field.concrete:
                    field_name = field.name
                    field_value = getattr(item, field_name)
                    if field_name in field_mapping:
                        item_data[field_mapping[field_name]] = field_value
                    else:
                        item_data[field_name] = field_value

            items_with_fields.append(item_data)
            
# Criando a Lista de Publishers:
    elif entity == 'publisher':
        name_tbl = 'PUBLISHERS'
        field_mapping = {
        'publisher_name': 'Nome',
        'publisher_year': 'Ano de Criação',
        'enterprise_pub': 'Direitos de Distribuição'
        }

        items = Publisher.objects.all()
        item_pk = Publisher.objects.first()
        fields = [field.name for field in Publisher._meta.get_fields()]  
        for item in items:
            item_data = {}
            for field in Publisher._meta.get_fields():
                if field.concrete:
                    field_name = field.name
                    field_value = getattr(item, field_name)
                    if field_name in field_mapping:
                        item_data[field_mapping[field_name]] = field_value
                    else:
                        item_data[field_name] = field_value

            items_with_fields.append(item_data)
    else:
        items = Game.objects.all()  # Deixei o padrão para jogos, mas pode ser alterado.

    return render(request, 'listar_dados.html', {
        'items': items, 
        'entity': entity,
        'fields': fields, 
        'items_with_fields': items_with_fields,
        'nome_tabela': name_tbl,
        'item_pk': item_pk,
        })
