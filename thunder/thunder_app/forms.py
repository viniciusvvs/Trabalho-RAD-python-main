from django import forms
class CadastroForm(forms.Form):
    nome = forms.CharField(label='Nome')
    email = forms.EmailField(label='Email')
    senha = forms.CharField(label='Senha', widget=forms.PasswordInput)
