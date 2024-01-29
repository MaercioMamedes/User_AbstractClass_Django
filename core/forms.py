from django import forms
from django.forms import PasswordInput
from django.core.exceptions import ValidationError


class CreateUserForm(forms.Form):
    first_name = forms.CharField(max_length=100, label="Nome")
    last_name = forms.CharField(max_length=100, label="Sobrenome")
    rg = forms.CharField(label="RG")
    cpf = forms.CharField(label="CPF")
    email = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=PasswordInput, label="Senha", required=True)
    password_confirm = forms.CharField(widget=PasswordInput, label="confirme a senha", required=True)

    def clean(self):
        cleaned_data = super().clean()
        cpf = cleaned_data.get('cpf')
        if cpf == 'teste':
            raise ValidationError("deu ruim")

        return cleaned_data
