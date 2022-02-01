# -----------------------------------------------------------------------------------------
# Ler as opções do menu prinicipal com tratamento de erros
# -----------------------------------------------------------------------------------------

def leiaOpções(num=4):
    op = (1, 2, 3, 4)
    while True:
        try:
            pergunta = int(input(num))
        except (ValueError, TypeError):
            print(f'\033[1;31mERRO! Digite uma opção válida\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\n\033[1;31mO usuário decidiu não digitar valores\033[m')
            break
        while pergunta not in op:
            print(f'\033[1;31mERRO! Digite uma opção válida\033[m')
            pergunta = int(input(num))
            continue
        else:
            return pergunta

# -----------------------------------------------------------------------------------------
# Ler números inteiros com tratamento de erros
# -----------------------------------------------------------------------------------------

def leiaInt(num=0):
    while True:
        try:
            pergunta = int(input(num))
        except (ValueError, TypeError):
            print(f'\033[1;31mERRO! Digite um número inteiro válido\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\n\033[1;31mO usuário decidiu não digitar valores\033[m')
            break
        else:
            return pergunta

# ------------------------------------------------------------------------------------------
# Ler números reais com tratamento de erros
# ------------------------------------------------------------------------------------------

def leiaFloat(num=0):
    while True:
        try:
            pergunta = input(num).replace(',', '.')
            conversor = float(pergunta)
        except (ValueError, TypeError):
            print(f'\033[1;31mERRO! Digite um número real válido\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\n\033[1;31mO usuário decidiu não digitar valores\033[m')
            break
        else:
            return conversor
