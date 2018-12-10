from django import forms
from django.forms import ModelForm
from .models import *

class AgricultorForm(ModelForm):
    
    class Meta:
        model = Agricultor
        fields = '__all__'
    
    def clean_qtd_credito(self):
        credito=self.cleaned_data['qtd_credito']

        if credito <= 0:
            raise forms.ValidationError('Quantidade de creditos nula ou negativa')
        else:
            return credito 

class EmprestimoForm(ModelForm):

    class Meta:
        model = Emprestimo
        fields = '__all__'
    
    def clean_qtd_emprestimo(self):
        emprestimo = self.cleaned_data['qtd_emprestimo']

        if emprestimo <= 0:
            raise forms.ValidationError('Quantidade de emprestimo nula ou negativa')
        else:
            return emprestimo

    def __init__(self,*args,**kwargs):
        super(EmprestimoForm,self).__init__(*args,**kwargs)

class BancoForm(ModelForm):

    class Meta:
        model = Banco
        fields = '__all__'

class TipoCulturaForm(ModelForm):

    class Meta:
        model = TipoCultura
        fields = '__all__'