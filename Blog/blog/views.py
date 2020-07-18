from django.shortcuts import render, HttpResponse, redirect

from .models import Post, Autor, Assunto, Assinatura
from django import forms
from .forms import PostForm
from django.contrib import messages 


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


def login(request):
    
    if request.method == 'POST':
        try:
            a = Autor.objects.filter(usuario = request.POST.get('usuario')).first()
            if a.senha == request.POST.get('senha'):
                request.session['autor_id'] = a.id
                return redirect('/')
            else:
                return HttpResponse("Senha incorreta!")
        except:
            return HttpResponse("Erro ao logar-se")
    else:
        return render(request, "login.html")


def logout(request):
    if 'autor_id' in request.session:
        del request.session['autor_id']
    
    return redirect('/')


def escrever(request):
    if 'autor_id' not in request.session:
        return redirect('/')

    if request.method == "POST":    
        form = PostForm(request.POST)
        if form.is_valid():
            p = Post()
            p.titulo = form.cleaned_data['titulo']
            p.assunto = form.cleaned_data['assunto']
            p.conteudo = form.cleaned_data['conteudo']
            p.autor = request.session['autor_id']
            p.save()
            return HttpResponse('Entrou aqui porra!')
        else:
            p = PostForm()
    
    context = {'form': form}
    return render(request, "escrever.html", context)