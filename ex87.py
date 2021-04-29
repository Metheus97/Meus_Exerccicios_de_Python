matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = valpar = mai = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digi de o numero que ficara na [{l},{c}]: '))
        if matriz[l][c] % 2 == 0:
            valpar += matriz[l][c]
        if c == 2:
            soma += matriz[l][c]
        if l == 2:
            if matriz[l][c] > mai:
                mai = matriz[l][c]
print('☺=' * 15)
for p in range(0, 3):
    for c in range(0, 3):
        print(f'[ {matriz[p][c]:^5} ]', end='')
    print()
print('☺=' * 15)
print(f'A soma dos valores da 3ª coluna é = {soma}')
print(f'A soma dos valores pares é = {valpar}')
print(f'O maior valor da segunda linha é = {mai}')
