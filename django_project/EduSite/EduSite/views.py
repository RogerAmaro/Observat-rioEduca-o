
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import LoginForm
# Create your views here.
from django.contrib.auth.forms import UserCreationForm # Formulario de criacao de usuarios
from django.contrib.auth.forms import AuthenticationForm # Formulario de autenticacao de usuarios
from django.contrib.auth import login 
from django.shortcuts import render

import pandas as pd
import numpy as np

def inicio(request):
    return render(request,"index.html")



def metas(request):
    xls = pd.ExcelFile("static/files/Ficha_de_Monitoramento_e_Avaliação_dos_PMEs_2018_final.xls")
    metas = Meta(xls, 'Meta 1').I_A
    prevista = metas[0]
    executada =  metas[1]
    return render(request,"metas.html", {'meta_prevista':prevista,'meta_executada':executada})


class Meta:
    def __init__(self,xls_file,sheet_name):
        self.df1 = pd.read_excel(xls_file,sheet_name) 
        self.years = ['2014','2015','2016','2017','2018','2019','2020','2021','2022','2023','2024','2025','2026'] 
        self.I_A = self.indicador(14,15)
        self.I_B = self.indicador(19,20)                     
        self.I_C = self.indicador(24,25) 
        self.I_D = self.indicador(29,30) 

    def indicador(self,line_1, line_2):
        meta_prevista = [x for x in self.df1.loc[line_1][3:16]]
        for i in meta_prevista:
            if np.isnan(i):
                meta_prevista[meta_prevista.index(i)]=0
                
        meta_executada =[ x for x in self.df1.loc[line_2][3:16]]
        for i in meta_executada:
            if np.isnan(i):
                meta_executada[meta_executada.index(i)]=0
    
        meta_executada = [ round(x,2) for x in meta_executada]
        meta_prevista = [  round(x,2) for x in meta_prevista]
        return [meta_prevista,meta_executada]

    



      
    
