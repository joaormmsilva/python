aluno = {}
alunos = []

while True:
    aluno ['nome'] = input('Digite seu nome: ')
    aluno ['nota1'] = float(input('Digite sua primeira nota: '))
    aluno ['nota2'] = float(input('Digite sua segunda nota: '))
    aluno ['media'] = (aluno['nota1'] + aluno['nota2']) / 2
    alunos.append(aluno.copy())
    veri = input("quer continuar ? [s/n]: ")
    if veri in 'nN':
        break
    
for m in range(len(alunos)):
    if alunos[m]['media'] < 6:
        alunos[m]['situação'] = 'reprovado'
    else:
        alunos[m]['situação'] = 'aprovado'
        
print('\nRELATÓRIO FINAL')
print(f'{"NOME":<10} {"MÉDIA":>6} {"SITUAÇÃO":>10}')
print('-' * 35)

for c in alunos:
    print(f'{c['nome']:<10} {c['media']:>6.1f} {c['situação']:>10}')