from django.shortcuts import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Game, Enterprise, Publisher, Dev
from .forms import GameForm, EnterpriseForm, DevForm, PublisherForm

# Create your views here.

# Funções  para acessar o BD e manipular os dados

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

def add_jogos (request):
    if request.method == 'POST':
     form = GameForm(request.POST)
     if form.is_valid():
        form.save()
        return redirect('listar_dados')
    else:
        form = GameForm()
    return render (request, 'add_jogos.html', {'form': form})


def atualizar_jogos(request, pk):
    games = get_object_or_404(Game, pk=pk)
    if request.method == 'POST':
        form = GameForm(request.POST, instance=games)
        if form.is_valid():
           form.save()
        return redirect('listar_dados')
    else:
        form = GameForm(instance=games)
        return render(request, 'atualizar_jogos.html', {'form': form, 'games': games})


def detalhar_jogos (request, pk):
    var_key1 = True
    var_key2 = False
    var_key3 = False
    var_key4 = False
    var_keys = (var_key1, var_key2, var_key3, var_key4)
    games = get_object_or_404(Game, pk=pk)
    return render(request, 'detalhes_jogos.html', {'games': games, 'var_keys': var_keys})

def excluir_jogos(request, pk):
    games = get_object_or_404(Game, pk=pk)
    if request.method in ['POST', 'GET']:
        games.delete()
    return redirect('listar_dados')

# Funções para acessar o BD das Empresas

def listar_emp(request):
    var_key1 = False
    var_key2 = True
    var_key3 = False
    var_key4 = False
    var_keys = (var_key1, var_key2, var_key3, var_key4)
    emp = Enterprise.objects.all() 
    return render(request, 'listar_dados.html', {'empresa': emp, 'var_keys': var_keys})

def add_emp (request):
    name_tbl = "Empresa"
    if request.method == 'POST':
     form = EnterpriseForm(request.POST)
     if form.is_valid():
        form.save()
        return redirect('/list/?entity=enterprise')
    else:
        form = EnterpriseForm()
    return render (request, 'add_jogos.html', {'form': form, 'nome_tabela': name_tbl})

def atualizar_emp(request, pk):
    emp = get_object_or_404(Enterprise, pk=pk)
    if request.method == 'POST':
        form = EnterpriseForm(request.POST, instance=emp)
        if form.is_valid():
           form.save()
        return redirect('/list/?entity=enterprise')
    else:
        form = EnterpriseForm(instance=emp)
        return render(request, 'atualizar_jogos.html', {'form': form, 'empresa': emp})

def detalhar_emp (request, pk):
    var_key1 = False
    var_key2 = True
    var_key3 = False
    var_key4 = False
    var_keys = (var_key1, var_key2, var_key3, var_key4)
    emp = get_object_or_404(Enterprise, pk=pk)
    return render(request, 'detalhes_jogos.html', {'empresa': emp, 'var_keys': var_keys})

def excluir_emp (request, pk):
    emp = get_object_or_404(Enterprise, pk=pk)
    if request.method in ['POST', 'GET']:
        emp.delete()
    return redirect('/list/?entity=enterprise')


# Funções para acessar o BD das Publisher
def listar_pub(request):
    var_key1 = False
    var_key2 = False
    var_key3 = True
    var_key4 = False
    var_keys = (var_key1, var_key2, var_key3, var_key4)
    pub = Publisher.objects.all() 
    return render(request, 'listar_dados.html', {'publishers': pub, 'var_keys': var_keys})

def add_pub (request):
    if request.method == 'POST':
     form = PublisherForm(request.POST)
     if form.is_valid():
        form.save()
        return redirect('/list/?entity=publisher')
    else:
        form = PublisherForm()
    return render (request, 'add_jogos.html', {'form': form})

def atualizar_pub(request, pk):
    pub = get_object_or_404(Publisher, pk=pk)
    if request.method == 'POST':
        form = PublisherForm(request.POST, instance=pub)
        if form.is_valid():
           form.save()
        return redirect('/list/?entity=publisher')
    else:
        form = PublisherForm(instance=pub)
        return render(request, 'atualizar_jogos.html', {'form': form, 'publisher': pub})

def detalhar_pub (request, pk):
    var_key1 = False
    var_key2 = False
    var_key3 = True
    var_key4 = False
    var_keys = (var_key1, var_key2, var_key3, var_key4)
    pub = get_object_or_404(Publisher, pk=pk)
    return render(request, 'detalhes_jogos.html', {'publisher': pub, 'var_keys': var_keys})

def excluir_pub (request, pk):
    pub = get_object_or_404(Publisher, pk=pk)
    if request.method in ['POST', 'GET']:
        pub.delete()
    return redirect('/list/?entity=publisher')


# Funções para acessar o BD das Desenvolvedores
def listar_devs(request):
    var_key1 = False
    var_key2 = False
    var_key3 = False
    var_key4 = True
    var_keys = (var_key1, var_key2, var_key3, var_key4)
    devs = Dev.objects.all() 
    return render(request, 'listar_dados.html', {'devs': devs, 'var_keys': var_keys})

def add_dev (request):
    if request.method == 'POST':
     form = DevForm(request.POST)
     if form.is_valid():
        form.save()
        return redirect('/list/?entity=dev')
    else:
        form = DevForm()
    return render (request, 'add_jogos.html', {'form': form})

def atualizar_dev(request, pk):
    dev = get_object_or_404(Dev, pk=pk)
    if request.method == 'POST':
        form = DevForm(request.POST, instance=dev)
        if form.is_valid():
           form.save()
        return redirect('/list/?entity=dev')
    else:
        form = DevForm(instance=dev)
        return render(request, 'atualizar_jogos.html', {'form': form, 'devs': dev})

def detalhar_dev (request, pk):
    var_key1 = False
    var_key2 = False
    var_key3 = False
    var_key4 = True
    var_keys = (var_key1, var_key2, var_key3, var_key4)
    dev = get_object_or_404(Dev, pk=pk)
    return render(request, 'detalhes_jogos.html', {'devs': dev, 'var_keys': var_keys})

def excluir_dev (request, pk):
    dev = get_object_or_404(Dev, pk=pk)
    if request.method in ['POST', 'GET']:
        dev.delete()
    return redirect('/list/?entity=dev')


