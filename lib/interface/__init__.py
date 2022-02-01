from lib.funcionalidades import *
from time import sleep

# ------------------------------------------------------------------------
# Mensagens prontas
# ------------------------------------------------------------------------

def mensagem(txt):
    qnt = len(txt) + 4
    print('~'*qnt)
    print(txt.center(qnt))
    print('~'*qnt)

# ------------------------------------------------------------------------
# Mostrar valor e produtos comprados
# ------------------------------------------------------------------------

def final():
    count = 0
    try:
        arq2 = open('dadosTemp.txt', 'r')
        txt = 'RESUMO DA COMPRA'
        print('~'*115)
        print(txt.center(115))
        print('~'*115)
        for linha in arq2:
            dado = linha.split(';')
            dado[3] = dado[3].replace('\n', '')
            converte2 = float(dado[3])
            count += converte2
            print('-'*115)
            print(f'Código: {dado[0]:<20} Produto: {dado[1]:<20} Quantidade: {dado[2]:<20} Total: R${dado[3]:<20}')
            sleep(0.5)
        print('-'*115)
        print(f'Total da Compra: R${count}')
        dinheiro = leiaFloat('Digite o dinheiro recebido: ')
        conta = dinheiro - count
        if conta == 0:
            print('Não é necessário troco')
        else:
            print(f'Troco: R${conta}')
    except:
        print('Houve um erro ao abrir o arquivo')
    finally:
        arq2 = open('dadosTemp.txt', 'w')
        arq2.write('')
    