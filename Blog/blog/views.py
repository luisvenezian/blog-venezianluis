from django.shortcuts import render, HttpResponse, redirect
import json
from .models import Post, Autor, Assunto, Assinatura, Comentario
from django import forms
from .forms import PostForm, AutorForm
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
            p.conteudo = form.cleaned_data['conteudo']
            p.autor = Autor.objects.get(id = request.session['autor_id'])   
            p.save()

            assunto = form.cleaned_data['assunto']
            for a in assunto:
                p.assunto.add(Assunto.objects.filter(assunto = a).first())
            # p.assunto.add(Assunto.objects.get(id=form.cleaned_data['assunto']))
            return redirect('/')
        else:
            return HttpResponse(form.errors)
    
    p = PostForm()    
    context = {'form': p}
    return render(request, "escrever.html", context)


def gostar(request):

    if request.is_ajax and request.method == "GET":
        postid = request.GET.get('postid')
        p = Post.objects.get(id = postid)
        a = Autor.objects.get(id = request.session['autor_id']) 
        data = {
            "gostaram" : 0,
            "classe" : ""
        }
        if a in p.gostaram.all():
            p.gostaram.remove(a)
            data.update({"gostaram" : p.quantos_gostaram()})
        else:
            p.gostaram.add(a)
            data.update({"gostaram" : p.quantos_gostaram(), "classe" : "gostou"})

        p.save()
        return HttpResponse(json.dumps(data))
    else:
        return HttpResponse('deu pau')


def cadastro(request):

    if request.method == "POST":    
        form = AutorForm(request.POST)
        if form.is_valid():
            a = Autor()
            a.nome = form.cleaned_data['nome']
            a.email = form.cleaned_data['email']
            a.usuario = form.cleaned_data['usuario'] 
            a.senha = form.cleaned_data['senha'] 
            a.apelido = form.cleaned_data['apelido'] 
            a.save()
            request.session['autor_id'] = a.id
            return redirect('/')
        else:
            return HttpResponse(form.errors)

    a = AutorForm()    
    context = {'form': a}
    return render(request, "cadastro.html", context)

def comentarios(request):

    data = {}

    if request.is_ajax and request.method == "GET":
        postid = request.GET.get('postid')
        comentarios = Comentario.objects.filter(post_id = postid) 

        if bool(comentarios):
            for c in comentarios:
                data.update({c.id : {"autor" : c.autor.nome, 
                                    "pic": str(c.autor.pic), 
                                    "comentario" : c.comentario, 
                                    "data" : str(c.data)}})


    return HttpResponse(json.dumps(data))