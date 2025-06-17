import random   

aluno1 = input("digite o nome dos alunos que vao participar: ")
aluno2 = input("digite o nome dos alunos que vao participar: ")
aluno3 = input("digite o nome dos alunos que vao participar: ")

alunos = [aluno1,aluno2,aluno3]

escolhido = random.choice(alunos)
print('O aluno sorteado para apagar a lousa é {}'.format(escolhido))

#--------------------------------------------------------------

pessoas = ['pedro', 'joao', 'victor', 'mathues']
escolhido = random.choice(pessoas)
print('O aluno sorteado para apagar a lousa é {}'.format(escolhido))

#--------------------------------------------------------------

aluno = input("digite o nome dos alunos que vao participar: ").split()
escolhidos = random.choice(aluno)
print('O aluno sorteado para apagar a lousa é: {}'.format(escolhidos))
