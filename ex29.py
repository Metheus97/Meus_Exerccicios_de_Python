numero = int(input('\033[35mEscolha um número:\033[m '))

div = numero % 2
if div == 0:
    print('O numero escolhido é \033[36m PAR')
else:
    print('O numero escolhido é \033[31mIMPAR')
