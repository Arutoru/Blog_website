from django import forms
from .models import Post, Comment
from django.db import models


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author','title', 'category', 'text', 'image')
        # les classes dans attrs permet d'avoir des widget prédéfinis, à partir du CSS
        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'category': forms.Select(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }
