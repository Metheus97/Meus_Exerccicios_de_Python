from ex115.lib.interface import *
from time import sleep

while True:
    açao = menu(['Cadastrar pessoas', 'Ver lista de pessoas', 'Sair do programa'])
    if açao == 1:
        cabeçalho('Cadastrar pessoas')
    elif açao == 2:
        cabeçalho('Ver lista de pessoas')
    elif açao == 3:
        cabeçalho('Sair do programa... Até logo!')
        break
    else:
        print('\033[31mERRO! Comando invalido.\033[m')
    sleep(1.5)
