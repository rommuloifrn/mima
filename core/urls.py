from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', HomeView.as_view()),
    
    path('cadastro', CadastroView.as_view(), name='cadastro'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    
    path('dashboard', DashboardView.as_view(), name='dashboard'),
    path('perfil/<str:pk>', PerfilView.as_view(), name='perfil'),
    path('adiciona-amigo', EnviaAmizadeView.as_view(), name='adiciona-amigo')
]

