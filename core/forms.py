from django.forms import Form, ModelForm
from .models import Sugestao, Amigo

class SugestaoForm(ModelForm):
    class Meta:
        model = Sugestao
        fields = [
            'nome', 'link', 'descricao'
        ]
        
# class RegistroForm(Form):
#     arroba = django.forms.CharField(max_length=20, required=True)
#     senha = django.forms.CharField(widget=forms.PasswordInput, max_length=50, required=True)

class RegistroForm(ModelForm):
    class Meta:
        model = Amigo
        fields = [
            'username', 'email', 'password'
        ]