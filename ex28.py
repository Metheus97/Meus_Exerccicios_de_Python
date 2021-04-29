vel = int(input('Qual a velocidade do carro: '))
print('*-*-'*30)
if vel > 80:
    multa = (vel - 80) * 7
    print('\033[1;31m Velocidade acima do permitido! Você esta sendo multado no valor de R${:.2f}'.format(multa))
else:
    print('\033[1;32m Você esta dentro da velocidade permitida, Obrigado por dirigir com segurança')
