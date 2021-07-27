from time import sleep

paleta = ['\033[m',  # 0- Sem cor
          '\033[41m',  # 1- Vermelho
          '\033[42m',  # 2- Verde
          '\033[43m',  # 3- Amarelo
          '\033[44m',  # 4- Azul
          '\033[45m',  # 5- Roxo
          '\033[46m',  # 6- Branco
          ]


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(paleta[cor], end='')
    print('-+' * tam)
    print(f'  {msg}')
    print('-+' * tam)
    print(paleta[0], end='')
    sleep(1)


def ajuda(com):
    titulo(f'Manual da função \'{com}\'', 4)
    print(paleta[3], end='')
    help(com)
    sleep(1)


# Programa principal
comando = ''
while True:
    titulo('SISTEMA PyHELP', 2)
    comando = str(input('Função Biblioteca >'))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('SISTEMA FINALIZADO', 1)