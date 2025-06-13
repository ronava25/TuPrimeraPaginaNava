from django import forms
from .models import Page

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['title', 'subtitle', 'content', 'image']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control w-25 bg-dark text-light border-secondary'
            }),
            'subtitle': forms.TextInput(attrs={
                'class': 'form-control w-25 bg-dark text-light border-secondary'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control w-25 bg-dark text-light border-secondary',
                'rows': 3
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control w-25 bg-dark text-light border-secondary'
            }),
        }
