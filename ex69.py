print('=' * 30)
print('Banco do Theus'.center(30))
print('=' * 30)
valor = int(input('Qual valor deseja sacar: R$ '))
cedula = 100
totcedula = 0
while True:
    if cedula <= valor:
        valor -= cedula
        totcedula += 1
    else:
        if totcedula != 0:
            print(f'Saira {totcedula} notas de {cedula}')
        if cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 2
        elif cedula == 2:
            cedula = 1
        totcedula = 0
        if valor == 0:
            break
