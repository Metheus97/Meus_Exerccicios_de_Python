tabela = ('Sombra',20,
          'Mascara de Cilios',13,
          'Pincel',3,
          'Mouse',33,
          'Teclado',50)
print('-'*40)
print(f'{"LISTA DE PRODUTOS":^40}')
print('-'*40)
for pos in range(0,len(tabela)):
    if pos % 2 == 0:
        print(f'{tabela[pos]:.<25}', end='')
    else:
        print(f'R${tabela[pos]:>8.2f}')
print('-'*40)
