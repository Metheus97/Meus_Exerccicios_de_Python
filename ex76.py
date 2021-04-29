valor = []
maior = menor = 0
for c in range(0, 5):
    valor.append(int(input(f'Valor da posição {c}:')))
    if c == 0:
        maior = menor = valor[c]
    else:
        if valor[c] > maior:
            maior = valor[c]
        if valor[c] < menor:
            menor = valor[c]
print('*-' * 30)
print(f'Você digitou o valor {valor}')
print(f'O MAIOR valor digitado é : {maior} Na posiçao:', end='')
for i, j in enumerate(valor):
    if j == maior:
        print(f' {i}...',end='')
print()
print(f'O MENOR valor digitado é: {menor} Na posiçao:', end='')
for i, j in enumerate(valor):
    if j == menor:
        print(f'{i}...', end='')
print()