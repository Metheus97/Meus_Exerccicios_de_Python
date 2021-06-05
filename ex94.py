"""Coleta de dados de pessoas e calculo de media de idade"""
# listas e dicionarios
pessoas = {}
grup = []
idade = 0

# coleta de dados
while True:
    pessoas['nome'] = str(input('Nome: '))
    while True:
        pessoas['sexo'] = str(input('Sexo:[M/F] ')).upper()
        if pessoas['sexo'] in 'FM':
            break
        print('ERRO! Selecione F ou M.')
    pessoas['idade'] = int(input('Idade: '))
    idade += pessoas['idade']
    grup.append(pessoas.copy())
    while True:
        res = (str(input('Deseja cadastrar mais pessoas?[S/N] '))).upper()
        if res in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N. ')
    if res in 'N':
        break

print('♦-' * 30)

# Exibir dados
nun = len(grup)
media = idade / nun


print(f'A) Ao todo temos {nun} pessoas cadastradas.')
print(f'B) A média de idade é de { media : .2f} anos.')
print(f'C) As mulheres cadastradas são: ', end='')
for p in grup:
    if p['sexo'] in 'F':
        print(f'{p["nome"]}, ', end='')
print()
print('D) lista de pessoas que estao acinma da média.')
for p in grup:
    if p['idade'] >= media:
        print('  ', end='')
        for k, v in p.items():
            print(f'{k} = {v}, ', end='')
        print()








