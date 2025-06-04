aluno = {}
alunos = []

while True:
    aluno ['nome'] = input('Digite seu nome: ')
    aluno ['nota1'] = int(input('Digite sua primeira nota'))
    aluno ['nota2'] = int(input('Digite sua segunda nota'))
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
print(f'{"No.":<4} {"NOME":<10} {"MÉDIA":>6} {"SITUAÇÃO":>10}')
print('-' * 35)
for i, a in enumerate(alunos):
    print(f'{i:<4} {a["nome"]:<10} {a["media"]:>6.1f} {a["situação"]:>10}')
print('-' * 35)