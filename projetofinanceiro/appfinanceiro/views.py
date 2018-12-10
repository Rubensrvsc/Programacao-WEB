from django.shortcuts import render,redirect
from .forms import *
from .models import *
# Create your views here.
def index(request):
    return render(request,'index.html')

def list_agricultor(request):
    agricultores = Agricultor.objects.all()
    return render(request,'list_agricultor.html',{'agricultor':agricultores})

def list_emprestimo(request):
    emprestimos = Emprestimo.objects.all()
    return render(request,'list_emprestimo.html',{'emprestimo':emprestimos})

def form_emprestimo(request):
    if request.method == 'POST':
        emprestimoform = EmprestimoForm(request or None)
        if emprestimoform.is_valid():
            emprestimoform.save()
            return redirect('index')
    else:
        emprestimoform=EmprestimoForm()
    return render(request,'form_emprestimo.html',{'formemprestimo':emprestimoform})

def form_agricultor(request):
    if request.method == 'POST':
        agricultorform = AgricultorForm(request or None)
        if agricultorform.is_valid():
            agricultorform.save()
            return redirect('index')
    else:
        agricultorform = AgricultorForm()
    return render(request,'form_agricultor.html',{'formagricultor':agricultorform})
