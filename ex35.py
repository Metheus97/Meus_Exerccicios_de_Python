numero = int(input('Digite um numero inteiro:'))
print('''Escolha uma da bases para conversão: 
 [ 1 ] converter para BINÁRIO
 [ 2 ] converter para OCTAL
 [ 3 ] converter para HEXADECIMAL''')
opcao = int(input('sua opçao: '))
if opcao == 1:
    print('{} convertido para BINARIO é igual a {}'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('\033[31mEsta opção não existe!')
