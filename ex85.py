num = [[], []]
col = 0
for n in range(0, 7):
    col = int(input(f'Digite o {n+1}º numero: '))
    if col%2 == 1:
        num[0].append(col)
    else:
        num[1].append(col)
num[0].sort()
num[1].sort()
print(f'Numeros impares da lista são {num[0]}')
print(f'Numeros pares da lista são {num[1]}')
