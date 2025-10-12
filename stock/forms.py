from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import AdaptedUser, Product, Message, Order

class AdaptedUserCreationForm(UserCreationForm):
    class Meta:
        model = AdaptedUser
        fields = [
            'name', 'username', 'cpf', 'address', 'birthDate', 'email', 'password'
        ]
        widgets = {
            'name' : forms.TextInput,
            'username' : forms.TextInput,
            'cpf' : forms.TextInput,
            'address' : forms.TextInput,
            'birthDate' : forms.DateInput,
            'email' : forms.EmailInput,
            'password' : forms.TextInput,
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'placeholder' : 'Senha'})
        self.fields['password2'].widget.attrs.update({'placeholder' : 'Confirme sua senha'})
    

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)