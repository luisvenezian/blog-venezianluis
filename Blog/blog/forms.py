from django import forms
from .models import Post, Autor
# from ckeditor.widgets import CKEditorWidget


class PostForm(forms.ModelForm):
    #assuntos = Assunto.objects.all()
    #assunto = forms.ModelChoiceField(queryset=assuntos, empty_label="Assunto", required=True)
    #assunto = forms.ChoiceField(choices=[('0', '--Selecione--')]+    [(assunto.id, assunto.assunto) for assunto in Assunto.objects.all()])

    class Meta:
        model = Post
        fields = ['titulo', 'assunto', 'conteudo']
        widgets = {
            'titulo' : forms.TextInput(
                attrs = {
                    'class' : 'form-control'
                }
            ),
            'assunto' : forms.CheckboxSelectMultiple(
                attrs = {
                    #'class' : 'form-control'
                }
            )
        }

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome', 'usuario','apelido', 'senha', 'email']
        widgets = {
            'nome' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder': 'Insira seu nome completo'
                }
            ),
            'usuario' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'O usuário será utilizado para logar-se!'
                }
            ),
            'apelido' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Insira como quer ser visto pela comunidade'
                }
            ),
            'senha' : forms.PasswordInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : '4S3nham41zD1Fi¢I!D0_ODNUM_'
                }
            ),
            'email' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder':'Insira um endereço válido'
                }
            )
        }