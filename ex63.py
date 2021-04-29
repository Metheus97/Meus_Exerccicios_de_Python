n1 = num = cont = maior = menor = 0
seg = 'S'
while seg != 'N' and seg == 'S':
    num = int(input('Digite um numero: '))
    seg = str(input('Quer continuar ? [S/N]: ')).upper()
    cont += 1
    n1 += num
    if cont == 1:
        maior = menor = num
    else:
        if num >= maior:
            maior = num
        if num <= menor:
            menor = num
print('Você digitou {} numeros e a media entre eles foi de {}'.format(cont, n1/cont))
print(f'O maior valor foi {maior} e o menor valor {menor}')
 