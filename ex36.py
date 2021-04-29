num1 = int(input('Digite um numero:'))
num2 = int(input('Agora outro:'))
if num1 > num2:
    maior = num1
    print('{} é maior'.format(maior))
if num2 > num1:
    maior = num2
    print('{} é maior'.format(maior))
if num2 < num1:
    menor = num2
    print('{} é menor'.format(menor))
if num1 < num2:
    menor = num1
    print('{} é menor'.format(menor))

if num1 == num2:
    print('Sao iguais')