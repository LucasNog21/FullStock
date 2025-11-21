from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import AdaptedUser, Product, Message, Order


class AdaptedUserCreationForm(UserCreationForm):
    class Meta:
        model = AdaptedUser
        fields = [
            "name",
            "username",
            "cpf",
            "address",
            "birthDate",
            "email",
            "password1",
            "password2",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Nome completo"}),
            "username": forms.TextInput(attrs={"placeholder": "Usuário"}),
            "cpf": forms.TextInput(attrs={"placeholder": "CPF"}),
            "address": forms.TextInput(attrs={"placeholder": "endereço"}),
            "birthDate": forms.DateInput(attrs={"placeholder": "Data de nascimento"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget.attrs.update({"placeholder": "Senha"})
        self.fields["password2"].widget.attrs.update(
            {"placeholder": "Confirme sua senha"}
        )


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "quantity",
            "allotment",
            "dueDate",
            "salePrice",
            "productionPrice",
            "description",
            "image",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Nome do produto"}),
            "quantity": forms.TextInput(attrs={"placeholder": "Quantidade"}),
            "allotment": forms.TextInput(attrs={"placeholder": "Lote do produto"}),
            "dueDate": forms.DateInput(attrs={"placeholder": "Data de vencimento"}),
            "salePrice": forms.TextInput(attrs={"placeholder": "Preço de venda"}),
            "productionPrice": forms.TextInput(
                attrs={"placeholder": "Preço de produção"}
            ),
            "description": forms.TextInput(attrs={"placeholder": "Descrição"}),
            "image": forms.FileInput(),
        }


class ProductFilterForm(forms.Form):
    initial_price = forms.FloatField(required=False, label="Preço inicial")
    final_price = forms.FloatField(required=False, label="Preço final")
    name = forms.CharField(required=False, label="Nome")
    description = forms.CharField(required=False, label="Descrição")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["initial_price"].widget.attrs.update(
            {
                "class": "form-control",
                "type": "number",
                "step": "0.01",
                "placeholder": "Preço mínimo",
            }
        )
        self.fields["final_price"].widget.attrs.update(
            {
                "class": "form-control",
                "type": "number",
                "step": "0.01",
                "placeholder": "Preço máximo",
            }
        )

        self.fields["name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Buscar por nome..."}
        )

        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Buscar por descrição..."}
        )
