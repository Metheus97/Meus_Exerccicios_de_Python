import moeda

num = float(input('Digite o preço R$ '))
print(f'O dobro de R${num} é R${moeda.dobro(num)}')
print(f'A metade de R${num} é R${moeda.metade(num)}')
print(f'Aumentando 10% no valor R${num} fica R${moeda.aumentar(num, 10)}')
print(f'Diminuindo 15% no valor R${num} fica R${moeda.diminuir(num, 15)}')
