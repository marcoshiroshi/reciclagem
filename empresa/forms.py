from django import forms
from django.core.exceptions import ValidationError
from core.utils import tools
from core.models import Estado
from empresa.models import Empresa, PontoColeta


class EmpresaDadosForm(forms.ModelForm):

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

    def clean_cnpj(self):
        cnpj = self.cleaned_data['cnpj'].replace('.', '').replace('-', '').replace('/', '')
        if self.instance.cnpj != cnpj:
            if not tools.cnpj_verification(cnpj):
                raise ValidationError('CNPJ inválido')
            if Empresa.objects.filter(cnpj=cnpj).exists():
                raise ValidationError('Este CNPJ já foi cadastrado no sistema.')
        return cnpj

    class Meta:
        model = Empresa

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cnpj': forms.TextInput(attrs={'class': 'form-control cnpj', 'placeholder': '00.000.000/0000-00'}),
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
            'nome',
            'cnpj',
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


class PontoColetaForm(forms.ModelForm):

    class Meta:
        model = PontoColeta

        widgets = {
            'tipo_aceito': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '-00,000000000000000', 'id': 'latitude'}),
            'longitude': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '-00,000000000000000', 'id': 'longitude'}),
        }

        fields = [
            'tipo_aceito',
            'longitude',
            'latitude',
        ]
