from blog.models import Post, Assunto

def linha_do_tempo(request):
    posts = Post.objects.order_by('-dt_postagem')

    linha_do_tempo = []
    for post in posts:
        arguments = [post.dt_postagem.strftime('%B')," ",str(post.dt_postagem.year)]
        
        # Somente distintos
        if "".join(arguments) not in linha_do_tempo:
            linha_do_tempo.append("".join(arguments))

    return {"linha_do_tempo": linha_do_tempo}

def menu(request):
    assuntos = Assunto.objects.filter(eh_menu = True).order_by('assunto')

    menu = []
    for item in assuntos:
        menu.append(item.assunto)

    return {"menu": menu}

def autenticado(request):
    return {"autenticado" : True if 'autor_id' in request.session else False}