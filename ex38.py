n1 = float(input('Nota da A1:'))
n2 = float(input('Nota da A2:'))
media = (n1 + n2) / 2
print('Sua media é {}'.format(media))
if media >= 7:
    print('Você foi APROVADO')
elif media >= 4 and media < 7:
    print('Você esta de recuperaçao')
else:
    print('Reprovado')
