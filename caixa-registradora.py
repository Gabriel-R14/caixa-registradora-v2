from time import sleep
from lib.interface import *
from lib.database import *
from lib.funcionalidades import *

while True:
    arquivo() # Abre o arquivo ou cria-o caso não exista
    mensagem('MENU PRINCIPAL')
    opções = leiaOpções('[ 1 ] Cadastro\n[ 2 ] Caixa\n[ 3 ] Gerenciar produtos\n[ 4 ] Sair\n--> ') # Menu principal
    if opções == 1:
        mensagem('CADASTRO')
        code = input('Digite o código do produto: ')
        pdt = input('Digite o nome do produto: ')
        valor = leiaFloat('Digite o valor do produto: R$')
        escrever(code, pdt, valor) # Cadastra o produto
    if opções == 2:
        mensagem('CAIXA')
        while True:
            código = input('Informe o código do produto: ')
            quantidade = leiaInt('Digite a quantidade: ')
            caixa(código, quantidade) # Cadastra temporariamente a compra (é apagado ao final da comrpa)
            continuar = input('Continuar: [S/N] ').upper().strip()[0]
            while continuar not in 'SN':
                continuar = input('Continuar: [S/N] ').upper().strip()[0]
            if continuar == 'N':
                final()
                sleep(1)
                break
    if opções == 3:
        while True:
            mensagem('LISTAGEM DE PRODUTOS')
            sleep(0.5)
            opções2 = leiaOpções('[ 1 ] Lista de produtos\n[ 2 ] Sair\n--> ')
            if opções2 == 1:
                ler() # Faz uma litsagem dos produtos cadastrados
            if opções2 == 2:
                sleep(0.5)
                mensagem('VOLTANDO AO MENU PRINCIPAL...')
                sleep(1)
                break
    if opções == 4:
        sleep(0.5)
        mensagem('SAINDO DO SISTEMA...')
        sleep(1)
        break
