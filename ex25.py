fr = str(input('Digite uma frase: ')).strip().upper()
print('A letra "A" aparece: {}'.format(fr.count('A')))
print('Preimeira apariçao é na posiçao: {}'.format(fr.find('A')))
print('Ultima apariçao é na posiçao: {}'.format(fr.rfind('A')))