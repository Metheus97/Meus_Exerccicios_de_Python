print('-=' * 15)
print('PROGRESSAO ARITIMETICA')
print('=-' * 15)
num1 = int(input('Incio:'))
num2 = int(input('Razao: '))
decimo = num1 + (10 - 1) * num2
for c in range(num1, decimo + num2, num2):
    print(c, end=' -> ')
