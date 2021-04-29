from random import choice
n1 = str(input('Nome da pessoa: '))
n2 = str(input('Nome da pessoa: '))
n3 = str(input('Nome da pessoa: '))

lista = [n1, n2, n3]
print('A pessoa mais BONITA é:{}'.format(choice(lista)))
