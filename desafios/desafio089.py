aluno = []

while True:
    nome = str(input('Digite seu nome: '))
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1 + nota2) / 2
    
    aluno.append([nome, [nota1, nota2], media])
    
    ver = input('Quer continuar? [S/N]: ').lower()
    if ver == 'n':
        break

print('=-' * 30)
print(f'{"No.":<4} {"NOME":<8} {"MÉDIA":>10}')
print('-' * 26)

for p, c in enumerate(aluno):
    print(f'{p:<4} {c[0]:<8} {c[2]:>10.1f}')

print('-' * 30)

while True:
    ver = int(input('Mostrar notas de qual aluno? (Digite 999 para sair): '))
    if ver == 999:
        print('Finalizando...')
        break
    if ver >= len(aluno):
        print('Aluno não existe. Tente novamente.')
    else:
        print(f'Notas do(a) {aluno[ver][0]} são {aluno[ver][1]}')
