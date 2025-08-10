from django import forms
from .models import Tarefa
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['titulo', 'descricao', 'concluida']

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)