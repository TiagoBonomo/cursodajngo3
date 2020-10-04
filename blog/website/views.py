from django.shortcuts import render


# Create your views here.
def hello_blog(request):

    #lista de Tecnologias
    lista = [
        'Django','Python','Git','Html','Banco de Dados',
        'Linux','Nginx','Uwsgi','Systemctl'
    ]
    #Dicionário de dados
    data = {
        'name':'Curso de Django 3',
        'lista_tecnologias': lista
    }
    return render(request,'index.html', data)
