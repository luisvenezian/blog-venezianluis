from django import forms
from .models import Post
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