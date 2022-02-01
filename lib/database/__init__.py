from time import sleep
from lib.funcionalidades import *

# -----------------------------------------------------------------------------------------
# Abrir database principal ou cria-la caso não exista
# ------------------------------------------------------------------------------------------

def arquivo():
    try:
        arq = open('dados.txt', 'r')
    except FileNotFoundError:
        arq = open('dados.txt', 'a+')

# ------------------------------------------------------------------------------------------
# Cadastrar produtos
# ------------------------------------------------------------------------------------------

def escrever(c=0, n='Produto inválido', v=0):
    try:
        arq = open('dados.txt', 'a')
        arq.write(f'{c};{n};{v}\n')
    except:
        print('Houve um erro ao cadastrar o produto')

# --------------------------------------------------------------------------------------------
# Listar os produtos cadastrados
# --------------------------------------------------------------------------------------------

def ler():
    try:
        arq = open('dados.txt', 'r')
        for linha in arq:
            dado = linha.split(';')
            dado[2] = dado[2].replace('\n', '')
            print('-'*80)
            print(f'Código: {dado[0]:<20} Produto: {dado[1]:<20} Preço: R${dado[2]:<20}')
            sleep(0.5)
    except:
        print('Houve um erro ao abrir o arquivo')

# -------------------------------------------------------------------------------------------
# Realizar compra
# -------------------------------------------------------------------------------------------

def caixa(codigo, quant):
    try:
        arq = open('dados.txt', 'r')
        arq2 = open('dadosTemp.txt', 'a+') # Arquivo temporário para fazer a compra
        for linha in arq:
            dado = linha.split(';')
            dado[2] = dado[2].replace('\n', '')
            if dado[0] == codigo:
                converte = float(dado[2])
                preço = quant * converte
                arq2.write(f'{dado[0]};{dado[1]};{quant};{preço}\n')
    except:
        print('Houve um erro ao realizar a compra')
