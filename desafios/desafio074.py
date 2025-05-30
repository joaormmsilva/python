import random
numeros =[]

for c in range(5):
    numero = random.randint(0,10)
    numeros.append(numero)
    
numeros.sort()

print(f'Os numeros gerados foram {numeros} o maior numero é {numeros[0]} e o menor numero {numeros[-1]}')

