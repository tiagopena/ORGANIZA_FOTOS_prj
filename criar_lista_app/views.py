from django.shortcuts import render
from .models import Manipulando_arquivos_class
from csv import reader
import os


def menu(request):
    conteudo = {
        'x' : 'x'
    }

    return render(request, 'menu.html', context=conteudo)

def gerar_lista(request):
    if request.POST:
        lista_arquivos = Manipulando_arquivos_class.gerar_lista_todos_arquivos(str(request.POST['origem_lista']),request.POST['descricao_drive'])
        Manipulando_arquivos_class.cria_arquivo_lista_todos_arquivos(lista_arquivos,request.POST['descricao_drive'])
        
    return render(request, 'gerar_lista.html')

def comparar_lista(request):
    resultado_csv = ''
    
    if request.POST:
        descricao_hd_01 = str(request.FILES['arquivo_json_01']).split('.')[0]
        descricao_hd_02 = str(request.FILES['arquivo_json_02']).split('.')[0]

        resultado = Manipulando_arquivos_class.comparar_listas(request.FILES['arquivo_json_01'],request.FILES['arquivo_json_02'])
        resultado_csv = Manipulando_arquivos_class.criar_arquivo_resultado(resultado,descricao_hd_01,descricao_hd_02)

    conteudo = {
        'resultado' : resultado_csv,
    }    

    return render(request, 'comparar_lista.html', context=conteudo)

def mostrar_resultado(request):
    lista_resultado = ''
    
    if request.POST:
        arquivo_resultado = str(request.FILES['arquivo_json_resultado'])

        with open((os.getcwd() + '/arquivos/' + arquivo_resultado), 'r') as arquivo:
            arquivo_csv = reader(arquivo)
            lista_resultado = list(arquivo_csv)
            arquivo.close()
        
        #resultado_csv = reader(request.FILES['arquivo_json_resultado'])

        #print(resultado_csv)

    conteudo = {
        'resultado' : lista_resultado,
    }    

    return render(request, 'mostrar_resultado.html', context=conteudo)
