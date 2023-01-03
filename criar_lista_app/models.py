from django.db import models
from pathlib import Path,PurePath
import pandas as pd
import json
import os
from csv import reader

class Manipulando_arquivos_class(models.Model):
    def gerar_lista_todos_arquivos (caminho_drive,descricao_drive):
        pasta = Path(caminho_drive)
        origem = descricao_drive
        lista_arquivos = []
        item_lista = {}

        for arquivo in pasta.glob('**/*'):
            if arquivo.is_file():
                drive  = PurePath(arquivo).drive
                nome_arquivo = arquivo.name
                extencao_arquivo = PurePath(arquivo).suffix
                nome_sem_extencao = PurePath(arquivo).stem
                caminho_absoluto = arquivo.absolute()
                identificador_dispositivo = arquivo.stat().st_dev
                tamanho_arquivo = arquivo.stat().st_size

                item_lista = {
                    'origem' : origem,
                    'drive' : drive,
                    'nome_arquivo' : nome_arquivo,
                    'extencao_arquivo' : extencao_arquivo,
                    'nome_sem_extencao' : nome_sem_extencao,
                    'caminho_absoluto' : str(caminho_absoluto),
                    'identificador_dispositivo' : identificador_dispositivo,
                    'tamanho_arquivo' : tamanho_arquivo
                }
                lista_arquivos.append(item_lista)

        return(lista_arquivos)

    def cria_arquivo_lista_todos_arquivos(lista_arquivos,descricao_drive):
        with open (os.getcwd() + '/arquivos/' + descricao_drive + '.json', 'w', encoding='utf-8') as arquivo_json:
            json.dump(lista_arquivos, arquivo_json, ensure_ascii=False, indent=2)
            arquivo_json.close()

    def comparar_listas(arquivo_json_01,arquivo_json_02):
        colunas_intercessao = ['nome_sem_extencao','tamanho_arquivo']

        data_frame_01 = pd.read_json(arquivo_json_01)
        data_frame_02 = pd.read_json(arquivo_json_02)
        
        merge = pd.merge(data_frame_01, data_frame_02, on=colunas_intercessao, how='inner')
        
        return(merge)

    def criar_arquivo_resultado(resultado,nome_origem_01,nome_origem_02):
        colunas_resultado = ['origem_x','drive_x','nome_sem_extencao','extencao_arquivo_x','caminho_absoluto_x','caminho_absoluto_y']
        
        data_frame_resultado = pd.DataFrame(resultado, columns=colunas_resultado)
        
        resultado_csv = data_frame_resultado.to_csv(os.getcwd() + '/arquivos/resultado-' + nome_origem_01 + '--' + nome_origem_02 + '.csv',index=None)

        with open((os.getcwd() + '/arquivos/resultado-' + nome_origem_01 + '--' + nome_origem_02 + '.csv'), 'r') as arquivo:
            arquivo_csv = reader(arquivo)
            lista_resultado = list(arquivo_csv)
            arquivo.close()
            
            return(lista_resultado)

            