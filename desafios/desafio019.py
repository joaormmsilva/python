import random  

aluno = input("digite o nome dos alunos que vao participar: ")
alunos = aluno.split()
escolhido = random.choice(alunos)
print('O aluno sorteado para apagar a lousa é {}'.format(escolhido))



pessoas = ['pedro', 'joao', 'victor', 'mathues']
escolhido = random.choice(pessoas)
print('O aluno sorteado para apagar a lousa é {}'.format(escolhido))