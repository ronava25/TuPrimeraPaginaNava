from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['receiver', 'subject', 'body']
        labels = {
            'receiver': 'Destinatario',
            'subject': 'Asunto',
            'body': 'Mensaje',
        }
        widgets = {
            'subject': forms.TextInput(attrs={
                'class': 'form-control bg-dark text-light border-secondary'
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-control bg-dark text-light border-secondary',
                'rows': 5
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['receiver'].widget.attrs.update({
            'class': 'form-select bg-dark text-light border-secondary'
        })
