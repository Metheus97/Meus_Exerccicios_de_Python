print('Sequencia de fibonacci')
print('*='*25)
termos = int(input('Quantos termos deve ser exibidos: '))
t1 = 0
t2 = 1
print('-='*25)
print('{} → {} → '.format(t1, t2), end='')
cont = 3
while cont <= termos:
    t3 = t1 + t2
    print('{} → '.format(t3), end='')
    cont += 1
    t1 = t2
    t2 = t3
print('FIM')
print('-='*25)