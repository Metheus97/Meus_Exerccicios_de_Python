nome = str(input('Digite seu nome completo:')).upper().strip().split()
print('Seu primeiro nome é:{}'.format(nome[0].title()))
print('Seu ultimo nome é:{}'.format(nome[len(nome)-1].title()))
