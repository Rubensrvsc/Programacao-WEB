from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.utils import timezone
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def list_agricultor(request):
    agricultores = Agricultor.objects.all()
    return render(request,'list_agricultor.html',{'agricultor':agricultores})

def list_emprestimo(request):
    emprestimos = Emprestimo.objects.all()
    return render(request,'list_emprestimo.html',{'emprestimo':emprestimos})

def list_banco(request):
    bancos = Banco.objects.all()
    return render(request,'list_banco.html',{'banco':bancos})

def list_cultura(request):
    culturas = TipoCultura.objects.all()
    return render(request,'list_cultura.html',{'cultura':culturas})

def form_emprestimo(request):
    if request.method == 'POST':
        emprestimoform = EmprestimoForm(request.POST or None)
        if emprestimoform.is_valid():
            emprestimoinstance = emprestimoform.save(commit=False)
            emprestimoinstance.dt_emprestmo=timezone.now()
            emprestimoinstance.save()
            return redirect('index')
    else:
        emprestimoform=EmprestimoForm()
    return render(request,'form_emprestimo.html',{'formemprestimo':emprestimoform})

def form_agricultor(request):
    if request.method == 'POST':
        agricultorform = AgricultorForm(request.POST or None)
        if agricultorform.is_valid():
            agricultorform.save()
            return redirect('index')
    else:
        agricultorform = AgricultorForm()
    return render(request,'form_agricultor.html',{'formagricultor':agricultorform})

def form_banco(request):
    if request.method == 'POST':
        bancoform = BancoForm(request.POST or None)
        if bancoform.is_valid():
            bc = bancoform.save(commit=False)
            if Banco.objects.filter(nome_banco__contains=bc.nome_banco):
                return render(request,'erro.html')
            else:
                bc.save()
                return redirect('index')
    else:
        bancoform = BancoForm()
    return render(request, 'form_banco.html', {'formbanco':bancoform})

def form_cultura(request):
    if request.method == 'POST':
        culturaform = TipoCulturaForm(request.POST or None)
        if culturaform.is_valid():
            ct = culturaform.save(commit=False)
            if TipoCultura.objects.filter(nome_cultura__contains=ct.nome_cultura):
                return render(request,'erro.html')
            else:
                ct.save()
                return redirect('index')
    else:
        culturaform = TipoCulturaForm()
    return render(request, 'form_cultura.html', {'formcultura':culturaform})

def procura_banco(request):
    banco = request.GET['procura_banco']
    bancos = Banco.objects.filter(nome_banco__contains=banco)
    return render(request, 'list_banco.html', {'banco':bancos})
