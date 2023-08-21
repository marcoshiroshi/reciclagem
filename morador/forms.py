from django import forms
from morador.models import Morador


class MoradorDadosForm(forms.ModelForm):

    class Meta:
        model = Morador

        widgets = {
            'cpf': forms.TextInput(attrs={'class': 'form-control cpf', 'placeholder': '000.000.000-00'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control date', 'placeholder': 'DD/MM/AAAA'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'telefone_1': forms.TextInput(attrs={'class': 'form-control phone', 'placeholder': '(00) 00000-0000'}),
            'telefone_2': forms.TextInput(attrs={'class': 'form-control phone', 'placeholder': '(00) 00000-0000'}),
            'cep': forms.TextInput(attrs={'class': 'form-control cep'}),
            'municipio': forms.Select(attrs={'class': 'form-control js-select2'}),
            'logradouro': forms.TextInput(attrs={'class': 'form-control'}),
            'complemento': forms.TextInput(attrs={'class': 'form-control'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '-00,000000000000000', 'id': 'latitude'}),
            'longitude': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '-00,000000000000000', 'id': 'longitude'}),
        }

        fields = [
            'cpf',
            'data_nascimento',
            'genero',
            'telefone_1',
            'telefone_2',
            'cep',
            'logradouro',
            'complemento',
            'municipio',
            'longitude',
            'latitude',
        ]
