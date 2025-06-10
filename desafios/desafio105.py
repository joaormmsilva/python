def notas(msg):
    while True:
        aluno['nome'] = input('Nome do aluno: ')
        nota1 = int(input('Qual a nota da primeira prova do aluno: '))
        nota2 = int(input('Qual a nota da segunda prova do aluno: '))
        media.append(nota1)
        media.append(nota2)
        aluno['nota1'] = nota1
        aluno['nota2'] = nota2
        alunos.append(aluno)
        veri = input('Quer continuar?[s/n]: ').lower()
        if veri == 'n':
            break


aluno = {}
alunos = []
media = []

aluno = notas()

        
