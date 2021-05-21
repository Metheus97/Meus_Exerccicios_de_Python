alunos = {}
alunos['aluno'] = str(input('Qual o nome do aluno? '))
alunos['media'] = float(input(f'Qual foi a media de {alunos["aluno"]}? '))
if alunos['media'] <= 5.99:
    alunos['status'] = 'Reprovado'
elif 6 <= alunos['media'] <= 7:
    alunos['status'] = 'Esta de Recuperação'
else:
    alunos['status'] = 'Aprovado'
print('♦-'*30)

for v, k in alunos.items():
    print(f'-{v} igual a {k}')
