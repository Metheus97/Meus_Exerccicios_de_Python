matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c]=int(input(f'Digi de o numero que ficara na [{l},{c}]: '))
print('')
for p in range(0, 3):
    for c in range(0, 3):
        print(f'[ {matriz[p][c]:^5} ]',end='')
    print()

'''print(matriz[0])
print(matriz[1])
print(matriz[2])'''
