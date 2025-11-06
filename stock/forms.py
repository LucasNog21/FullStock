from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import AdaptedUser, Category, Provider, Product, Message, Order, Movement

class AdaptedUserCreationForm(UserCreationForm):
    class Meta:
        model = AdaptedUser
        fields = [
            'name', 'username', 'cpf', 'address', 'birthDate', 'email', 'password1', 'password2'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nome completo'}),
            'username': forms.TextInput(attrs={'placeholder': 'Usuário'}),
            'cpf': forms.TextInput(attrs={'placeholder': 'CPF'}),
            'address': forms.TextInput(attrs={'placeholder': 'Endereço'}),
            'birthDate': forms.DateInput(attrs={'type': 'date', 'placeholder': 'Data de nascimento'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'placeholder': 'Senha'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirme sua senha'})

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Usuário'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}))

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nome da categoria'}),
            'description': forms.TextInput(attrs={'placeholder': 'Descrição'}),
        }

class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = ['name', 'cnpj', 'contact', 'address']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nome do fornecedor'}),
            'cnpj': forms.TextInput(attrs={'placeholder': 'CNPJ'}),
            'contact': forms.TextInput(attrs={'placeholder': 'Contato'}),
            'address': forms.TextInput(attrs={'placeholder': 'Endereço'}),
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name', 'quantity', 'allotment', 'dueDate', 'salePrice', 'productionPrice',
            'description', 'sku', 'active', 'category', 'provider', 'local', 'image'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nome do produto'}),
            'quantity': forms.NumberInput(attrs={'placeholder': 'Quantidade'}),
            'allotment': forms.NumberInput(attrs={'placeholder': 'Lote'}),
            'dueDate': forms.DateInput(attrs={'type': 'date', 'placeholder': 'Data de vencimento'}),
            'salePrice': forms.NumberInput(attrs={'placeholder': 'Preço de venda'}),
            'productionPrice': forms.NumberInput(attrs={'placeholder': 'Preço de produção'}),
            'description': forms.Textarea(attrs={'placeholder': 'Descrição'}),
            'sku': forms.NumberInput(attrs={'placeholder': 'SKU'}),
            'local': forms.TextInput(attrs={'placeholder': 'Localização no estoque'}),
            'image': forms.FileInput(),
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['provider', 'product', 'orderDate', 'quantity', 'value', 'status']
        widgets = {
            'provider': forms.Select(),
            'product': forms.Select(),
            'orderDate': forms.DateInput(attrs={'type': 'date'}),
            'quantity': forms.NumberInput(attrs={'placeholder': 'Quantidade'}),
            'value': forms.NumberInput(attrs={'placeholder': 'Valor total'}),
            'status': forms.TextInput(attrs={'placeholder': 'Status do pedido'}),
        }

class MovementForm(forms.ModelForm):
    class Meta:
        model = Movement
        fields = ['product', 'type', 'quantity', 'date', 'reason', 'user']
        widgets = {
            'product': forms.Select(),
            'type': forms.Select(),
            'quantity': forms.NumberInput(attrs={'placeholder': 'Quantidade'}),
            'date': forms.DateInput(attrs={'type': 'date'}),
            'reason': forms.Select(),
            'user': forms.Select(),
        }

class ProductFilterForm(forms.Form):
    initial_price = forms.FloatField(required=False, label="Preço inicial")
    final_price = forms.FloatField(required=False, label="Preço final")
    name = forms.CharField(required=False, label='Nome')
    description = forms.CharField(required=False, label='Descrição')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['initial_price'].widget.attrs.update({
            'class': 'form-control',
            'type': 'number',
            'step': '0.01',
            'placeholder': 'Preço mínimo'
        })
        self.fields['final_price'].widget.attrs.update({
            'class': 'form-control',
            'type': 'number',
            'step': '0.01',
            'placeholder': 'Preço máximo'
        })

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Buscar por nome...'
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Buscar por descrição...'
        })
