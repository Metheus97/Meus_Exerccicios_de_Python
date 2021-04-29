valor = []

for c in range(0,5):
    v = (int(input(f'Adicione o {c + 1}º numero a lista: ')))
    if c == 0 or v > valor[-1]:
        valor.append(v)
    else:
        pos = 0
        while pos < len(valor):
            if v <= valor[pos]:
                valor.insert(pos, v)
                break
            pos += 1

print('=*' * 30)
print(valor)





