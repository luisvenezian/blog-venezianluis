from django import forms
from .models import Post
# from ckeditor.widgets import CKEditorWidget


class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'autor' : forms.Select(
                attrs = {
                    'class' : 'form-control'
                }
            ),
            'titulo' : forms.TextInput(
                attrs = {
                    'class' : 'form-control'
                }
            ),
            'assunto' : forms.Select(
                attrs = {
                    'class' : 'form-control'
                }
            )
        }