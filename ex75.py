palavras = ('milionario','sucesso','gratidão','Deus','paz','amor','felicidade')
for p in palavras :
    print(f'\nNa palavra {p.upper()} tem as vogais ',end='')
    for letra in p:
        if letra.lower() in 'a e i o u':
            print(letra, end=' ')