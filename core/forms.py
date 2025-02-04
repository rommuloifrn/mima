from django.forms import Form, ModelForm
from .models import Sugestao

class SugestaoForm(ModelForm):
    class Meta:
        model = Sugestao
        fields = [
            'nome', 'link', 'descricao'
        ]