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
from appfinanceiro import views,views_alter

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

    path('edit_banco/<int:id_banco>',views_alter.banco_edit,name='editbanco'),
    path('edit_emprestimo/<int:id_emprestimo>',views_alter.emprestimo_edit,name='editemprestimo'),
    path('edit_agricultor/<int:id_agricultor>',views_alter.agricultor_edit,name='editagricultor'),
    path('edit_cultura/<int:id_cultura>',views_alter.cultura_edit,name='editcultura'),

    path('<int:id_banco>',views_alter.deletar_banco,name='delete_banco'),
    path('<int:id_emprestimo>',views_alter.deletar_emprestimo,name='delete_emprestimo'),
    path('<int:id_agricultor>',views_alter.deletar_agricultor,name='delete_agricultor'),
    path('<int:id_cultura>',views_alter.deletar_cultura,name='delete_cultura'),
    
    path('procura_banco',views.procura_banco,name='procura_banco'),
]
