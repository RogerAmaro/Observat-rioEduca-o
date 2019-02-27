
# from django.shortcuts import render, render_to_response
# from django.http import HttpResponse, HttpResponseRedirect
# from django.contrib import messages
# from django.contrib.auth import authenticate, login
# from .forms import LoginForm
# # Create your views here.
# from django.contrib.auth.forms import UserCreationForm # Formulario de criacao de usuarios
# from django.contrib.auth.forms import AuthenticationForm # Formulario de autenticacao de usuarios
# from django.contrib.auth import login 
# from django.shortcuts import render

import pandas as pd
import numpy as np

# def inicio(request):
#     return render(request,"index.html")


xls = pd.ExcelFile("/home/lab-pesquisa/Desktop/projetos/graficos_planilha/Ficha de Monitoramento e Avaliação dos PMEs 2018_final.xls") #### lembras de trocar pelo arquivo django

    


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
    
        meta_executada = [ x*100 for x in meta_executada]
        meta_prevista = [ x*100 for x in meta_prevista]
        return [meta_prevista,meta_executada]

    

#metas = Meta(xls,'Meta 20')
#print(metas.indicador(metas.I_XA[0],metas.I_XA[1]))
# print(metas.I_A)

print(Meta(xls,'Meta 7').I_C)

      
    
