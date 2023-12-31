from django import forms
from django.core.exceptions import ValidationError
from datetime import datetime
from core.utils import tools
from morador.models import Morador
from core.models import Estado, OrdemServico, ItemServico


class MoradorDadosForm(forms.ModelForm):

    def clean_data_nascimento(self):
        data_nascimento = self.cleaned_data['data_nascimento']
        if data_nascimento:
            if ((datetime.now().date() - data_nascimento).days)/356 <= 18:
                raise ValidationError('Não é possível cadastrar menores de idade')
        return data_nascimento

    def clean_telefone_1(self):
        telefone_1 = self.cleaned_data['telefone_1']
        if telefone_1:
            if tools.all_equal(list(telefone_1.replace('(', '').replace(')', '').replace(' ', '').replace('-', ''))):
                raise ValidationError('Telefone inválido!')
        return telefone_1

    def clean_telefone_2(self):
        telefone_2 = self.cleaned_data['telefone_2']
        if telefone_2:
            if tools.all_equal(list(telefone_2.replace('(', '').replace(')', '').replace(' ', '').replace('-', ''))):
                raise ValidationError('Telefone inválido!')
        return telefone_2

    def clean_cpf(self):
        cpf = self.cleaned_data['cpf'].replace('.', '').replace('-', '').replace('/', '')
        if self.instance.cpf != cpf:
            if not tools.cpf_verification(cpf):
                raise ValidationError('CPF inválido')
            if Morador.objects.filter(cpf=cpf).exists():
                raise ValidationError('Este CPF já foi cadastrado no sistema.')
        return cpf

    class Meta:
        model = Morador

        widgets = {
            'cpf': forms.TextInput(attrs={'class': 'form-control cpf', 'placeholder': '000.000.000-00'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control date', 'placeholder': 'DD/MM/AAAA'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'telefone_1': forms.TextInput(attrs={'class': 'form-control phone', 'placeholder': '(00) 00000-0000'}),
            'telefone_2': forms.TextInput(attrs={'class': 'form-control phone', 'placeholder': '(00) 00000-0000'}),
            'cep': forms.TextInput(attrs={'class': 'form-control cep_mask'}),
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

    estado = forms.ModelChoiceField(
        required=True,
        queryset=Estado.objects.all(),
        empty_label='Selecione uma opção',
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )


class MoradorItemServicoForm(forms.ModelForm):

    def clean_qtd(self):
        if self.cleaned_data.get('qtd') == 0:
            raise ValidationError('Quantidade inválida!')
        return self.cleaned_data.get('qtd')

    class Meta:
        model = ItemServico

        widgets = {
            'item': forms.Select(attrs={'class': 'form-control js-select2'}),
            'qtd': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade do mesmo item'}),
        }

        fields = [
            'item',
            'qtd',
        ]
