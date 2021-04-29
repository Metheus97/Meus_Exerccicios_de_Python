lista = []
res = "S"
while res == "S":
    n = int(input("Digite um numero: "))
    lista.append(n)
    res = str(input("Deseja adicionar mais?[S/N]")).upper()
lista.sort(reverse=True)
print("*-"*30)
if 5 in lista:
    print("Esta lista contem o numero 5!")
else:
    print("Esta lista não contem o numero 5")
print("*-"*30)
print(lista)
print("*-"*30)
print(f"Foram digitados {len(lista)}")
