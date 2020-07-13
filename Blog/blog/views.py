from django.shortcuts import render, HttpResponse
from .models import Post, Autor, Assunto, Assinatura
from django import forms

# Create your views here.
def home_page(request, assunto = False):

    dados = {
        "posts": Post.objects.order_by('-dt_postagem')
    }
    
    if assunto:
        try:
            dados.update({"posts" : dados['posts'].filter(assunto = Assunto.objects.get(assunto__iexact = assunto).id)})
        except:
            dados.update({"except" : True})

    if not dados['posts']:
        dados.update({"posts": Post.objects.order_by('-dt_postagem')})

    return render(request, "home.html", dados)

def cv(request):
    return HttpResponse('Curriculum Vitae')

def assinatura(request):

    retorno = {
            "situacao": "null",
            "resultado": "null" 
        }

    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')

        try:
            Assinatura.objects.create(nome = nome, email = email)
            retorno.update({
                "situacao": "Cadastrado com sucesso!",
                "resultado": "success"}
                )
        except Exception as e:
            if "duplicate" in str(e):
                retorno.update({"situacao": "jacad"})
            else:
                retorno.update({"situacao": "descon"})
            retorno.update({"resultado": "exception"})

    return render(request, "assinatura.html", retorno)