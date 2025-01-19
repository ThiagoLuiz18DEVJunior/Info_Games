from django.shortcuts import render, redirect, get_object_or_404
from .models import Game, Enterprise, Publisher, Dev
from .forms import GameForm, EnterpriseForm, DevForm, PublisherForm

# Create your views here.
# Variaveis de controle
# Página de Home

def home_page(request):
    return render(request, 'home_page.html')

# Funções para acessar o BD dos Jogos
def listar_jogos(request):
    var_key1 = True
    var_key2 = False
    var_key3 = False
    var_key4 = False
    var_keys = (var_key1, var_key2, var_key3, var_key4)
    games = Game.objects.all() 
    return render(request, 'listar_jogos.html', {'games': games, 'var_keys': var_keys})

def add_jogos (request):
    if request.method == 'POST':
     form = GameForm(request.POST)
     if form.is_valid():
        form.save()
        return redirect('listar_jogos')
    else:
        form = GameForm()
    return render (request, 'add_jogos.html', {'form': form})

def atualizar_jogos(request, pk):
    games = get_object_or_404(Game, pk=pk)
    if request.method == 'POST':
        form = GameForm(request.POST, instance=games)
        if form.is_valid():
           form.save()
        return redirect('listar_jogos')
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
    return redirect('listar_jogos')

# Funções para acessar o BD das Empresas

def listar_emp(request):
    var_key1 = False
    var_key2 = True
    var_key3 = False
    var_key4 = False
    var_keys = (var_key1, var_key2, var_key3, var_key4)
    emp = Enterprise.objects.all() 
    return render(request, 'listar_jogos.html', {'empresa': emp, 'var_keys': var_keys})

def add_emp (request):
    if request.method == 'POST':
     form = EnterpriseForm(request.POST)
     if form.is_valid():
        form.save()
        return redirect('listar_empresas')
    else:
        form = EnterpriseForm()
    return render (request, 'add_jogos.html', {'form': form})

def atualizar_emp(request, pk):
    emp = get_object_or_404(Enterprise, pk=pk)
    if request.method == 'POST':
        form = EnterpriseForm(request.POST, instance=emp)
        if form.is_valid():
           form.save()
        return redirect('listar_empresas')
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
    return redirect('listar_empresas')


# Funções para acessar o BD das Publisher
def listar_pub(request):
    var_key1 = False
    var_key2 = False
    var_key3 = True
    var_key4 = False
    var_keys = (var_key1, var_key2, var_key3, var_key4)
    pub = Publisher.objects.all() 
    return render(request, 'listar_jogos.html', {'publishers': pub, 'var_keys': var_keys})

def add_pub (request):
    if request.method == 'POST':
     form = PublisherForm(request.POST)
     if form.is_valid():
        form.save()
        return redirect('listar_pubs')
    else:
        form = PublisherForm()
    return render (request, 'add_jogos.html', {'form': form})

def atualizar_pub(request, pk):
    pub = get_object_or_404(Publisher, pk=pk)
    if request.method == 'POST':
        form = PublisherForm(request.POST, instance=pub)
        if form.is_valid():
           form.save()
        return redirect('listar_pubs')
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
    return redirect('listar_pubs')


# Funções para acessar o BD das Desenvolvedores
def listar_devs(request):
    var_key1 = False
    var_key2 = False
    var_key3 = False
    var_key4 = True
    var_keys = (var_key1, var_key2, var_key3, var_key4)
    devs = Dev.objects.all() 
    return render(request, 'listar_jogos.html', {'devs': devs, 'var_keys': var_keys})

def add_dev (request):
    if request.method == 'POST':
     form = DevForm(request.POST)
     if form.is_valid():
        form.save()
        return redirect('listar_devs')
    else:
        form = DevForm()
    return render (request, 'add_jogos.html', {'form': form})

def atualizar_dev(request, pk):
    dev = get_object_or_404(Dev, pk=pk)
    if request.method == 'POST':
        form = DevForm(request.POST, instance=dev)
        if form.is_valid():
           form.save()
        return redirect('listar_devs')
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
    return redirect('listar_devs')


