from django.http import HttpResponse

from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect # Funcao para redirecionar o usuario
from django.contrib.auth.forms import UserCreationForm # Formulario de criacao de usuarios
from django.contrib.auth.forms import AuthenticationForm # Formulario de autenticacao de usuarios
from django.contrib.auth import login # funcao que salva o usuario na sessao

def inicio(request):
    return render(request,"index.html")

def login(request):
    return render(request,"login.html")
