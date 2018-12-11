from django import forms
from django.forms import ModelForm
from .models import *

class AgricultorForm(ModelForm):
    
    class Meta:
        model = Agricultor
        fields = '__all__'
        widgets = {
            'nome_agricultor': forms.CheckboxSelectMultiple()
        }
    
    def clean_qtd_credito(self):
        credito=self.cleaned_data['qtd_credito']

        if credito <= 0:
            raise forms.ValidationError('Quantidade de creditos nula ou negativa')
        else:
            return credito 

class EmprestimoForm(ModelForm):

    class Meta:
        model = Emprestimo
        fields = ('qtd_emprestimo','juros','qtd_parcela','banco')
        widgets = {
            'banco': forms.CheckboxSelectMultiple()
        }
    
    def __init__(self,*args,**kwargs):
        super(EmprestimoForm,self).__init__(*args,**kwargs)
        self.fields['banco'].queryset = Banco.objects.all()
    
    def clean_qtd_emprestimo(self):
        qtd_emprestimo = self.cleaned_data['qtd_emprestimo']

        if qtd_emprestimo <= 0:
            raise forms.ValidationError('Quantidade de emprestimo nula ou negativa')
        else:
            return qtd_emprestimo

class BancoForm(ModelForm):

    class Meta:
        model = Banco
        fields = '__all__'

class TipoCulturaForm(ModelForm):

    class Meta:
        model = TipoCultura
        fields = '__all__'