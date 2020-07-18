from django.db import models
from readtime import of_html
from ckeditor.fields import RichTextField

# Create your models here.
# Criei toda essa merda no SQL pra descobrir isso só depois...

class Autor(models.Model):
    usuario = models.CharField(max_length=15)
    apelido = models.CharField(max_length=15)
    senha = models.CharField(max_length=32)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    email = models.TextField(max_length=200)
    pic = models.ImageField(upload_to = 'static/blog/pic_folder/', default = 'static/blog/pic_folder/None/no-img.jpg')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields = ['email'], name = 'unique_email_autor'),
            models.UniqueConstraint(fields = ['usuario'], name = 'unique_usuario_autor')
        ]

    def __str__(self):
        return self.nome

class Assunto(models.Model):
    assunto = models.CharField(max_length=30)
    eh_menu = models.BooleanField(default=None, blank=True, null=True)

    def __str__(self):
        return self.assunto

    class meta:
        constraints = [
            models.UniqueConstraint(fields=['assunto'], name='unique_assunto')
        ]

class Post(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    conteudo = RichTextField(blank = True, null = True)
    assunto = models.ManyToManyField(Assunto)
    dt_postagem = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return self.titulo 

    # Formata por exemplo para Jun 04. 3:30PM
    def dt_postagem_formatado(self):
        return self.dt_postagem.strftime("%b %d.  %I:%M%p")
    
    # Retorna um str de assuntos de uma publicação separados por virgula
    def assuntos(self):
        assuntos = ''
        ultimo = len(self.assunto.all())-1
        for i, item in enumerate(self.assunto.all()):
            assuntos += str(item) 
            if i != ultimo:
                assuntos += ', ' 

        return assuntos

    def tempo_de_leitura(self):
        return of_html(self.conteudo).text

class Assinatura(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    dt_assinatura = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return self.nome

    class Meta:
        constraints = [
            models.UniqueConstraint(fields = ['email'], name = 'unique_email'),
        ]