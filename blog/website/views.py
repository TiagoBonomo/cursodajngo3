from django.shortcuts import render
from .models import Post, Contact


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

def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request,'post_detail.html',{'post': post})

def save_form(request):
    name = request.POST['name']
    Contact.objects.create(
        name = name,
        email = request.POST['email'],
        message = request.POST['message']
    )
    return render(request,'contact_success.html',{ 'name_contact': name})