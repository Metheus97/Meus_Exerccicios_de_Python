from ex109 import moeda

num = float(input('Digite o preço R$ '))
print(f'O dobro de {moeda.moeda(num)} é {moeda.dobro(num)}')
print(f'A metade de {moeda.moeda(num)} é {moeda.metade(num)}')
print(f'Aumentando 10% no valor {moeda.moeda(num)} fica {moeda.aumentar(num, 10)}')
print(f'Diminuindo 15% no valor {moeda.moeda(num)} fica {moeda.diminuir(num, 15)}')