s = 0
c = 0
for impar in range(1, 500, 2):
    if impar % 3 == 0:
        s += impar
        c = c + 1
print('Soma dos {} valores solicitados sao de {}'.format(c, s))
