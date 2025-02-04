from django.shortcuts import render

from django.views import View

from django.contrib.auth.views import LoginView, LogoutView

from django import http

from .models import *

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
        user = Amigo.objects.get(username=kwargs['pk'])
        context = {
            'user': user,
            'sugestoes': user.item_set.all()
        }
        return render(request, 'core/perfil.html', context)
    
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
        amigo = Amigo.objects.create_user(
            request.POST['usuario'],
            request.POST['email'],
            request.POST['password']
        )
        
        amigo.save()
        login(request, amigo)
        return http.HttpResponseRedirect('/')
        ## redirecionar para o dashboard, usuário já logado