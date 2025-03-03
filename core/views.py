from django.shortcuts import render, HttpResponseRedirect

from django.views import View

from django.contrib.auth.views import LoginView, LogoutView

from django import http

from .models import *

from .forms import *

from django.contrib.auth import authenticate, login



# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, 'core/home.html')
    
class DashboardView(View):
    def get(self, request):
        amigos = reversed(request.user.de_quem_e_amigo.all())
        return render(request, 'core/dashboard.html', {'amigos':amigos})

class PerfilView(View):
    def get(self, request, *args, **kwargs):
        try:
            username=kwargs['pk']
        except KeyError:
            context = {
                'user': request.user,
            }
            return render(request, 'core/perfil.html', context)
            
        
        user = Amigo.objects.get(username=kwargs['pk'])
        context = {
            'user': user,
            'sugestoes': user.sugestao_set.all()
        }
        return render(request, 'core/perfil.html', context)
            

class AdicionarSugestaoView(View):
    def get(self, request):
        form = SugestaoForm()
        return render(request, 'core/c_sugestao.html', {'form':form})
        
    def post(self, request):
        form = SugestaoForm(request.POST)

        if form.is_valid():
            Sugestao.objects.create(
                amigo=request.user,
                nome=form.cleaned_data['nome'],
                link=form.cleaned_data['link'],
                descricao=form.cleaned_data['descricao']
            )
        return HttpResponseRedirect('perfil/'+str(request.user))
    
class EnviaAmizadeView(View):
    def post(self, request):
        pesquisa = request.POST.get('pesquisa')
        
        resultado = Amigo.objects.filter(username=pesquisa)
        
        if (resultado):
            Amizade.objects.create(remetente=request.user, destinatario=resultado[0])
            return http.HttpResponseRedirect('/dashboard')
        else:
            return  render(request, 'core/dashboard.html', {'erro':'foda'})

class LoginView(LoginView):
    template_name = 'core/auth/login.html'
    next_page = 'dashboard'
    
class LogoutView(LogoutView):
    next_page = ''
    template_name = 'core/auth/logout.html'

class CadastroView(View):
    def get(self, request):
        return render(request, 'core/auth/cadastro.html')
    
    def post(self, request, *args, **kwargs):
        form = RegistroForm(request.POST)
        if form.is_valid():
            amigo = Amigo.objects.create_user(
                form.cleaned_data['username'],
                form.cleaned_data['email'],
                form.cleaned_data['password']
            )
            
            login(request, amigo)
            return http.HttpResponseRedirect('/')
            ## redirecionar para o dashboard, usuário já logado
        else:
            return render(request, 'core/auth/cadastro.html', {'form':form})