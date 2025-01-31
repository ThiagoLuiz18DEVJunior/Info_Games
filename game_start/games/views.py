from django.shortcuts import *
from .user_view import *
from .models import *
from .forms import *
from django.urls import *
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
# Função Automática para Listar os Dados em um Arquivo HTML
# Create your views here.
# Função de Home Page

    
# Funções  para acessar o BD e manipular os dados

class DataList(TemplateView):
    template_name = 'listar_dados.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        model_choice = self.request.GET.get('model', 'game')  
  
        if model_choice == 'game':
            model = Game
            form_class = GameForm
        elif model_choice == 'enterprise':
            model = Enterprise
            form_class = EnterpriseForm
        elif model_choice == 'dev':
            model = Dev
            form_class = DevForm  
        elif model_choice == 'publisher':
            model = Publisher
            form_class = PublisherForm
        else: 
            model = Game
            form_class = GameForm

        items = model.objects.all()
        field_names = [field for field in form_class._meta.fields]
        field_label = {field: form_class._meta.labels.get(field) for field in field_names}
        items_with_fields = []

        for item in items:
            item_data = {}
            for field in model._meta.get_fields():
                if field.concrete:  
                    field_name = field.name
                    field_value = getattr(item, field_name)
                    if field_name in field_label:
                        item_data[field_label[field_name]] = field_value
                    else:
                        item_data[field_name] = field_value
            items_with_fields.append(item_data)

        context['items_with_fields'] = items_with_fields
        context['model_choice'] = model_choice
        return context

class DataListDetails(TemplateView):
    template_name = 'detalhar_dados.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        model_choice = self.request.GET.get('model', 'game')  

        if model_choice == 'game':
            model = Game
            form_class = GameForm
        elif model_choice == 'enterprise':
            model = Enterprise
            form_class = EnterpriseForm
        elif model_choice == 'dev':
            model = Dev
            form_class = DevForm  
        elif model_choice == 'publisher':
            model = Publisher
            form_class = PublisherForm
        else: 
            model = Game
            form_class = GameForm

        items = model.objects.all()
        field_names = [field for field in form_class._meta.fields]
        field_label = {field: form_class._meta.labels.get(field) for field in field_names}
        items_with_fields = []

        for item in items:
            item_data = {}
            for field in model._meta.get_fields():
                if field.concrete:
                    field_name = field.name
                    field_value = getattr(item, field_name)
                    
                    if field.many_to_many:
                        field_value = list(field_value.all()) 
                        field_value = [str(val) for val in field_value]
                    
                    if field_name in field_label:
                        item_data[field_label[field_name]] = field_value
                    else:
                        item_data[field_name] = field_value

            items_with_fields.append(item_data)

        # Passa as informações para o contexto
        context['items_with_fields'] = items_with_fields
        context['model_choice'] = model_choice
        return context

class DataAdd(LoginRequiredMixin, CreateView):
    template_name = 'add_dados.html'
    success_url = reverse_lazy('listar')
    
    def get_model(self):
        model_choice = self.request.GET.get('model', 'game')  
        if model_choice == 'game':
            return Game
        elif model_choice == 'enterprise':
            return Enterprise
        elif model_choice == 'dev':
            return Dev
        elif model_choice == 'publisher':
            return Publisher
        else:
            return Game  

    def get_form_class(self):
        model = self.get_model()
        if model == Game:
            return GameForm
        elif model == Enterprise:
            return EnterpriseForm
        elif model == Dev:
            return DevForm
        elif model == Publisher:
            return PublisherForm
        else:
            return GameForm  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_choice'] = self.request.GET.get('model', 'game')  
        return context

class DataAtt(LoginRequiredMixin, UpdateView):
    template_name = 'atualizar_dados.html'
    success_url = reverse_lazy('listar')

    def get_model(self):
        model_choice = self.kwargs.get('model', 'game')  
        if model_choice == 'game':
            return Game
        elif model_choice == 'enterprise':
            return Enterprise
        elif model_choice == 'dev':
            return Dev
        elif model_choice == 'publisher':
            return Publisher
        else:
            return Game

    def get_form_class(self):
        model = self.get_model()
        if model == Game:
            return GameForm
        elif model == Enterprise:
            return EnterpriseForm
        elif model == Dev:
            return DevForm
        elif model == Publisher:
            return PublisherForm
        else:
            return GameForm

    def get_object(self, queryset=None):
        model = self.get_model()
        object_id = self.kwargs.get('pk')  
        return get_object_or_404(model, pk=object_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_choice'] = self.kwargs.get('model', 'game') 
        return context

def home_page(request):
    return render(request, 'base.html')

def excluir_jogos(request, pk):
    games = get_object_or_404(Game, pk=pk)
    if request.method in ['POST', 'GET']:
        games.delete()
    return redirect('/listar/?model=games')


def excluir_emp (request, pk):
    emp = get_object_or_404(Enterprise, pk=pk)
    if request.method in ['POST', 'GET']:
        emp.delete()
    return redirect('/list/?model=enterprise')


def excluir_pub (request, pk):
    pub = get_object_or_404(Publisher, pk=pk)
    if request.method in ['POST', 'GET']:
        pub.delete()
    return redirect('/list/?model=publisher')


def excluir_dev (request, pk):
    dev = get_object_or_404(Dev, pk=pk)
    if request.method in ['POST', 'GET']:
        dev.delete()
    return redirect('/list/?model=dev')