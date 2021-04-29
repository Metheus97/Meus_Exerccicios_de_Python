print('VAMOS SOMAR !')
print('-'*30)
cont = ns = num = 0
num = int(input('Digite um o numero que deseja somar [999 finaliza] : '))
while num != 999:
    cont += num
    ns += 1
    num = int(input('Digite um o numero que deseja somar [999 finaliza] : '))
print('Você digitou {} Valores totalizando {}'.format(ns, cont))
