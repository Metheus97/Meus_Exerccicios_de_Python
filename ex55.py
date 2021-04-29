'''c = 1
while c != 'F' and c != 'M':
    c = str(input('Qual é seu sexo ? [F/M] : ')).upper()
    print('Sua resposta nao é valida, tente novamente!')

if c == 'F':
    print('Olá, senhorita!')
else:
    print('Olá, senhor!')'''

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))