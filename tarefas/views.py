from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa
from .forms import TarefaForm, RegistroForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.urls import reverse

# Lista de tarefas
@login_required
def lista_tarefas(request):
    pendentes = Tarefa.objects.filter(concluida=False, usuario=request.user)
    concluidas = Tarefa.objects.filter(concluida=True, usuario=request.user)
    return render(request, 'tarefas/lista.html', {
        'pendentes': pendentes,
        'concluidas': concluidas
    })

# Nova tarefa
@login_required
def nova_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.usuario = request.user
            tarefa.save()
            return redirect('lista_tarefas')
    else:
        form = TarefaForm()
    return render(request, 'tarefas/nova.html', {'form': form})

# Editar tarefa
@login_required
def editar_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id, usuario=request.user)
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('lista_tarefas')
    else:
        form = TarefaForm(instance=tarefa)
    return render(request, 'tarefas/editar.html', {'form': form})

# Excluir tarefa
@login_required
def excluir_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id, usuario=request.user)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('lista_tarefas')
    return render(request, 'tarefas/excluir.html', {'tarefa': tarefa})

# Registro de usuário (não requer login)
def registrar(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('lista_tarefas')
    else:
        form = RegistroForm()
    return render(request, 'tarefas/registro.html', {'form': form})

# Login de usuário (não requer login)
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['username']
            senha = form.cleaned_data['password']
            user = authenticate(request, username=usuario, password=senha)
            if user is not None:
                login(request, user)
                return redirect('lista_tarefas')
            else:
                form.add_error(None, 'Usuário ou senha inválidos.')
    else:
        form = LoginForm()
    return render(request, 'tarefas/login.html', {'form': form})

# Logout manual (opcional, pode remover se usar LogoutView no urls.py)
def logout_view(request):
    logout(request)
    return redirect('login')

# Alternar conclusão de tarefa
@login_required
def toggle_concluida(request, id):
    tarefa = get_object_or_404(Tarefa, id=id, usuario=request.user)
    tarefa.concluida = not tarefa.concluida
    tarefa.save()
    return HttpResponse(reverse('lista_tarefas'))



