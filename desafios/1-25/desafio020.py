import random

aluno = input("digite o nome dos grupos que vao participar: ")

grupos = aluno.split()
random.shuffle(grupos)

print('a ordem dos grupos sorteados é: ')
print(grupos)

#--------------------------------------------------------------

aluno1 = input("digite o nome do grupo: ")
aluno2 = input("digite o nome do grupo: ")
aluno3 = input("digite o nome do grupo: ")
grupo = [aluno1, aluno2, aluno3]
random.shuffle(grupo)

print('a ordem dos grupos sorteados é: ')
print(grupo)