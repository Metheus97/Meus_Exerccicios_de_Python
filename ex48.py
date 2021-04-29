s = 0
cont = 0
for c in range(1,7):
    num = int(input('Digite o {}º valor: '.format(c)))
    if num % 2 == 0:
        s += num
        cont += 1
print('você digitou {} numeros pares e a somatoria deles é de {}'.format(cont, s))

