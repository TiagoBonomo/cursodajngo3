from django.shortcuts import render
from .models import Post


# Create your views here.
def hello_blog(request):

    #Lista de posts vinda do Banco de Dados
    list_posts = Post.objects.filter(deleted=False)

    #lista de Tecnologias
    lista = [
        'Django','Python','Git','Html','Banco de Dados',
        'Linux','Nginx','Uwsgi','Systemctl'
    ]

    #Dicionário de dados
    data = {
        'name':'Curso de Django 3',
        'lista_tecnologias': lista,
        'posts':list_posts,
    }
    
    return render(request,'index.html', data)
