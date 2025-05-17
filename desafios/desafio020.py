import random

aluno = input("digite o nome dos grupos que vao participar: ")
grupos = aluno.split()
random.shuffle(grupos)

print('a ordem dos grupos sorteados é: ')
print(grupos)