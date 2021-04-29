numero = (int(input('Digite um numero :')),
          int(input('Digite Outro numero :')),
          int(input('Digite Mais um numero :')),
          int(input('Digite o ultimo numero :')))
print(f'Voce digitou os valores {numero}')
print(f'O numero 9 apareceu {numero.count(9)} vezes')
if 3 in numero:
    print(f'O numero 3 esta na {numero.index(3)+1}º posiçao')
else:
    print('O valor 3 nao foi digitado')
print(f'os numeros pares são os', end='')
for n in numero:
    if n % 2 ==0:
        print(f' {n}', end= '')

print(f'')
