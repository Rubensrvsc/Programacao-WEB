"""projetofinanceiro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appfinanceiro import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('lista_agricultor', views.list_agricultor, name='lista_agricultor'),
    path('lista_emprestimo', views.list_emprestimo, name='lista_emprestimo'),
    path('lista_banco', views.list_banco, name='lista_banco'),
    path('lista_cultura', views.list_cultura, name='lista_cultura'),
    path('agricultor', views.form_agricultor, name='formagricultor'),
    path('emprestimo', views.form_emprestimo, name='formemprestimo'),
    path('banco', views.form_banco, name='formbanco'),
    path('cultura', views.form_cultura, name='formcultura'),
    #path('procura<str:palavra>')
]
