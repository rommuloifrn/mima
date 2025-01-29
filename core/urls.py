from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', HomeView.as_view()),
    
    path('cadastro', CadastroView.as_view(), name='cadastro'),
    
    path('dashboard', DashboardView.as_view(), name='dashboard'),
    path('adiciona-amigo', EnviaAmizadeView.as_view(), name='adiciona-amigo')
]

