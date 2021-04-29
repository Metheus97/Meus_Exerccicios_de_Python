print('=-'*30)
print('CADASTRE PESSOAS')
print('=-'*30)
cont = homens = mulher = 0
while True:
    idade = int(input('Idade :'))
    sexo = fechar = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).upper().strip()[0]
    while fechar not in 'SN':
        fechar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if idade >= 18:
        cont += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F':
        if idade <= 20:
            mulher += 1
    if fechar == 'N':
        break
    print('=-'*30)
print('=-'*30)
print(f'Cadastrados temos\n {cont} pessoas com mais de 18 \n {homens} homens \n {mulher} mulheres com menos de 20 anos.')