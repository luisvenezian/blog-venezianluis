from django.contrib import admin

# Register your models here.
from .models import Autor, Post, Assunto, Assinatura
admin.site.register(Autor)
admin.site.register(Post)
admin.site.register(Assunto)
admin.site.register(Assinatura)