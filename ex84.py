pessoas = []
dados = []
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]

    else:
        if dados[1] >= maior:
            maior = dados[1]
        if dados[1] <= menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    cont = (str(input('Deseja continuar? [S/N] '))).upper()
    if cont in 'N':
        break

print('-º'*35)
print(f'Foram coletato os dados de {len(pessoas)} pessoas')
print('-º'*35)
print(f'O maior peso foi de {maior}Kg. Peso de', end='')
for p in pessoas:
    if p[1] == maior:
        print(f' {p[0]}')

print(f'\nO menor peso foi de {menor}Kg. Peso de', end='')
for x in pessoas:
    if x[1] == menor:
        print(f' {x[0]}')
print('-º'*35)
