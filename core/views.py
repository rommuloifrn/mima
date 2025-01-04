from django.shortcuts import render
from django.views import View

from django import http

from .models import Amigo

# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, 'core/home.html')

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
        return http.HttpResponseRedirect('/')