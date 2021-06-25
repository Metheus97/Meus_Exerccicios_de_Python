'''Progama para calcular área de terrenos quadrados'''


def area(l, c):
    a = l * c
    print(f'A área de um terreno de {l} X {c} é de {a}m².')


# Programa principal
print('    Calculo de Área')
print('-' * 30)
largura = float(input('LARGURA: '))
comprimento = float(input('COMPRIMENTO: '))
area(largura, comprimento)
