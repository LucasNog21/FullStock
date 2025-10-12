from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import AdaptedUser, Product, Message, Order

class AdaptedUserCreationForm(UserCreationForm):
    class Meta:
        model = AdaptedUser
        fields = [
            'name', 'username', 'cpf', 'address', 'birthDate', 'email', 'password1', 'password2'
        ]
        widgets = {
            'name' : forms.TextInput(attrs={'placeholder': 'Nome completo'}),
            'username' : forms.TextInput(attrs={'placeholder': 'Usuário'}),
            'cpf' : forms.TextInput(attrs={'placeholder': 'CPF'}),
            'address' : forms.TextInput(attrs={'placeholder': 'endereço'}),
            'birthDate' : forms.DateInput(attrs={'placeholder': 'Data de nascimento'}),
            'email' : forms.EmailInput(attrs={'placeholder': 'Email'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'placeholder' : 'Senha'})
        self.fields['password2'].widget.attrs.update({'placeholder' : 'Confirme sua senha'})
    

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)