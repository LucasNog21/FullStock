from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import AdaptedUser, Category, Provider, Product, Order, Sale

class AdaptedUserCreationForm(UserCreationForm):
    class Meta:
        model = AdaptedUser
        fields = [
            'name', 'username', 'cpf', 'address', 'birthDate', 'email', 'password1', 'password2'
        ]

        labels = {
            'name' : 'Nome',
            'username' : 'Apelido',
            'cpf' : 'CPF',
            'address': 'Endereço',
            'birthDate' : 'Data de nascimento',
            'email' : 'Email',
            'password1' : 'Senha',
            'password2' : 'Confirmação de senha'
        }

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

    labels = {
        'username' : 'Apelido',
        'password' : 'Senha',
    }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

        labels = {
            'name' : 'Nome',
            'description' : 'Descrição',
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nome da categoria'}),
            'description': forms.TextInput(attrs={'placeholder': 'Descrição'}),
        }

class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = ['name', 'cnpj', 'contact', 'address']

        labels = {
            'name' : 'Nome',
            'cnpj' : 'CNPJ',
            'contact' : 'Contato',
            'address' : 'Endereço'
        }

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

        labels = {
            'name': 'Nome',
            'quantity': 'Quantidade',
            'allotment': 'Lote',
            'dueDate': 'Data de vencimento',
            'salePrice': 'Preço de venda',
            'productionPrice': 'Preço de produção',
            'description': 'Descrição',
            'sku': 'SKU',
            'active': 'Ativo',
            'category': 'Categoria',
            'provider': 'Fornecedor',
            'local': 'Localização',
            'image': 'Imagem',
        }

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
        fields = ['provider', 'product', 'orderDate', 'quantity', 'status']

        labels = {
            'provider' : 'Fornecedor',
            'product' : 'Produto',
            'orderDate' : 'Data do pedido',
            'quantity' : 'Quantidade',
            'status' : 'Status'
        }
        widgets = {
            'provider': forms.Select(),
            'product': forms.Select(),
            'orderDate': forms.DateInput(attrs={'type': 'date'}),
            'quantity': forms.NumberInput(attrs={'placeholder': 'Quantidade'}),
            'status': forms.Select(),
        }

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['product', 'saleDate', 'quantity', 'user']

        labels = {
            'product' : 'Produto',
            'saleDate' : 'Data da venda',
            'quantity' : 'Quantidade',
            'user' : 'Usuário'
        }

        widgets = {
            'product': forms.Select(),
            'saleDate': forms.DateInput(attrs={'type': 'date'}),
            'quantity': forms.NumberInput(attrs={'placeholder': 'Quantidade'}),
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

class SalesFilterForm(forms.Form):
    product_name = forms.CharField(required=False, label="Produto")
    user_name = forms.CharField(required=False, label="Usuário")
    start_date = forms.DateField(required=False, label="Data inicial")
    end_date = forms.DateField(required=False, label="Data final")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['product_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Nome do produto'
        })
        self.fields['user_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Nome do usuário'
        })
        self.fields['start_date'].widget.attrs.update({
            'class': 'form-control',
            'type': 'date'
        })
        self.fields['end_date'].widget.attrs.update({
            'class': 'form-control',
            'type': 'date'
        })

STATUS_CHOICES = [
    ('', '--- Selecionar ---'),
    ('pending', 'Pendente'),
    ('approved', 'Aprovado'),
    ('rejected', 'Rejeitado'),
]
        

class OrderFilterForm(forms.Form):
    provider_name = forms.CharField(required=False, label="Fornecedor")
    product_name = forms.CharField(required=False, label="Produto")
    status = forms.ChoiceField(
        required=False,
        label="Status",
        choices=[('', '--- Selecionar ---')] + Order.STATUS
    )
    start_date = forms.DateField(required=False, label="Data inicial")
    end_date = forms.DateField(required=False, label="Data final")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['provider_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Nome do fornecedor'
        })
        self.fields['product_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Nome do produto'
        })
        self.fields['status'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['start_date'].widget.attrs.update({
            'class': 'form-control',
            'type': 'date'
        })
        self.fields['end_date'].widget.attrs.update({
            'class': 'form-control',
            'type': 'date'
        })

class ProviderFilterForm(forms.Form):
    name = forms.CharField(required=False, label="Nome")
    cnpj = forms.CharField(required=False, label="CNPJ")
    contact = forms.CharField(required=False, label="Contato")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Nome do fornecedor'
        })
        self.fields['cnpj'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'CNPJ'
        })
        self.fields['contact'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Telefone / Contato'
        })

class CategoryFilterForm(forms.Form):
    name = forms.CharField(required=False, label="Nome da categoria")
    description = forms.CharField(required=False, label="Descrição")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Nome da categoria'
        })
        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Descrição'
        })
