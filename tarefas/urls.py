from django.urls import path
from . import views

urlpatterns = [
    # Tarefas
    path('', views.lista_tarefas, name='lista_tarefas'),
    path('nova/', views.nova_tarefa, name='nova_tarefa'),
    path('editar/<int:id>/', views.editar_tarefa, name='editar_tarefa'),
    path('excluir/<int:id>/', views.excluir_tarefa, name='excluir_tarefa'),
    path('toggle/<int:id>/', views.toggle_concluida, name='toggle_concluida'),

    # Autenticação
    path('registrar/', views.registrar, name='registrar'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

]
