cid = str(input('Digite o nome da sua cidede:')).strip()

cid1 = (cid[:3].upper().replace('SÃO', 'SAO')) == 'SAO'

print(cid1)