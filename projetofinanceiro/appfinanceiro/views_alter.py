from django.shortcuts import render,redirect
from .forms import *
from .models import *

def banco_edit(request,id_banco):
    banco = Banco.objects.get(id=id_banco)
    if request.method == 'POST':
        bancoform = BancoForm(request.POST,instance=banco)
        if bancoform.is_valid():
            bancoform.save()
            return redirect('lista_banco')
    else:
        bancoform = BancoForm(instance=banco)
    return render(request,"edit_banco.html",{'formbanco':bancoform})

def emprestimo_edit(request,id_emprestimo):
    emprestimo = Emprestimo.objects.get(id=id_emprestimo)
    if request.method == 'POST':
        emprestimoform = EmprestimoForm(request.POST,instance=emprestimo)
        if emprestimoform.is_valid():
            emprestimoform.save()
            return redirect('lista_emprestmo')
    else:
        emprestimoform=EmprestimoForm(instance=emprestimo)
    return render(request,"edit_emprestimo.html",{'formemprestimo':emprestimoform})

def cultura_edit(request,id_cultura):
    cultura = TipoCultura.objects.get(id=id_cultura)
    if request.method == 'POST':
        culturaform = TipoCulturaForm(request.POST,instance=cultura)
        if culturaform.is_valid():
            culturaform.save()
            return redirect('lista_cultura')
    else:
        culturaform=TipoCulturaForm(instance=cultura)
    return render(request,"edit_cultura.html",{'formcultura':culturaform})

def agricultor_edit(request,id_agricultor):
    agricultor = Agricultor.objects.get(id=id_agricultor)
    if request.method == 'POST':
        agricultorform = AgricultorForm(request.POST,instance=agricultor)
        if agricultorform.is_valid():
            agricultorform.save()
            return redirect('lista_agricultor')
    else:
        agricultorform = AgricultorForm(instance=agricultor)
    return render(request,"edit_banco.html",{'formagricultor':agricultorform})

def deletar_banco(request, id_banco):
    Banco.objects.filter(id=id_banco).delete()
    return redirect('lista_banco')

def deletar_emprestimo(request, id_emprestimo):
    Emprestimo.objects.filter(id=id_emprestimo).delete()
    return redirect('lista_emprestimo')

def deletar_cultura(request, id_cultura):
    TipoCultura.objects.filter(id=id_cultura).delete()
    return redirect('lista_cultura')

def deletar_agricultor(request, id_agricultor):
    Agricultor.objects.filter(id=id_agricultor).delete()
    return redirect('lista_agricultor')