from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control bg-dark text-light border-secondary w-100'
            })

class ProfileForm(forms.ModelForm):
    email = forms.EmailField(label="Email", required=True)

    avatar = forms.ImageField(
        label="Modificar avatar",
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control bg-dark text-light border-secondary w-25'
        })
    )

    birth_date = forms.DateField(
        label="Fecha de nacimiento",
        widget=forms.DateInput(attrs={
            'type': 'text',
            'class': 'form-control bg-dark text-light border-secondary w-25',
            'placeholder': 'DD/MM/AAAA'
        }),
        input_formats=['%d/%m/%Y']
    )

    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'birth_date']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['email'].initial = user.email
            self.user = user

            self.fields['email'].widget.attrs.update({
                'class': 'form-control bg-dark text-light border-secondary w-25'
            })
            self.fields['avatar'].widget.attrs.update({
                'class': 'form-control bg-dark text-light border-secondary w-25'
            })
            self.fields['bio'].widget.attrs.update({
                'class': 'form-control bg-dark text-light border-secondary w-25',
                'rows': 3
            })
    def save(self, commit=True):
        profile = super().save(commit=False)

        if hasattr(self, 'user'):
            self.user.email = self.cleaned_data['email']
            if commit:
                self.user.save()

        if commit:
            profile.save()

        return profile

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control bg-dark text-light border-secondary w-100'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control bg-dark text-light border-secondary w-100'
    }))