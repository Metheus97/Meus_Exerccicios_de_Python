media = 0
maior = 0
nomevelho = ''
mulher = 0
for c in range(1, 5):
    print('*'*10, 'Dados da {}º Pessoa'.format(c), '*'*10)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [m/f]: '))
    media += idade
    if c == 1 and sexo == 'Mm':
        maior = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maior:
        maior = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulher += 1
print('A media de idade desse grupo de pessoas é de {} anos'.format(media/4))
print('O homen mais velho do grupo é o {} com {} anos'.format(nomevelho ,maior))
print('Temos {} mulheres com menos de 20 anos'.format(mulher))
