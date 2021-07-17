#primeiro input
frase = str(input('Digite o seu nome completo:')).strip()

#transformaçao
print(frase.upper())
print(frase.lower())

#contando letras
space = frase.count(' ')
letras = len(frase)
print('Seu nome tem {} letras'.format(letras - space))

nome1 = frase.split()
print('Seu primeiro nome é {} e tem {} letras'.format(nome1[0], len(nome1[0])))
