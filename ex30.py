viagem = float(input('Coloque o valor de sua viagem em Km:'))
if viagem > 200:
    valor = viagem * 0.45
    print('O valor da dua passagem ficou \033[36mR${:.2f}\033[m'.format(valor))
else:
    caro = viagem * 0.5
    print('O valor da sua passagem ficou \033[35mR${:.2f}\033[m'.format(caro))
